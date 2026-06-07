from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
import os
from pyspark.sql.window import Window
from pyspark.sql.functions import avg
from pyspark.sql.functions import lag
from pyspark.sql.functions import stddev
from pyspark.sql.functions import col
from pyspark.sql.functions import when

# start spark session
spark = SparkSession.builder \
    .appName("StockPreprocessing") \
    .getOrCreate()

# folder path
data_folder = "data/stock_data"

# get all csv files
files = os.listdir(data_folder)

all_data = None

print("\nLoading stock files...\n")

for file in files:

    if file.endswith(".csv"):

        file_path = f"{data_folder}/{file}"

        # stock name from filename
        stock_name = file.split("_")[0]

        print(f"Reading {file}...")

        # read csv
        df = spark.read.csv(
            file_path,
            header=True,
            inferSchema=True
        )

        # add stock column
        df = df.withColumn("Stock", lit(stock_name))

        # combine dataframes
        if all_data is None:
            all_data = df
        else:
            all_data = all_data.union(df)

# show schema
print("\nDataset Schema:\n")
all_data.printSchema()

# window for moving averages
window_spec = Window.partitionBy("Stock") \
    .orderBy("Date")

# 7 day moving average
ma7_window = window_spec.rowsBetween(-6, 0)

all_data = all_data.withColumn(
    "MA_7",
    avg("Close").over(ma7_window)
)

# 30 day moving average
ma30_window = window_spec.rowsBetween(-29, 0)

all_data = all_data.withColumn(
    "MA_30",
    avg("Close").over(ma30_window)
)

# 90 day moving average
ma90_window = window_spec.rowsBetween(-89, 0)

all_data = all_data.withColumn(
    "MA_90",
    avg("Close").over(ma90_window)
)

# previous close price
all_data = all_data.withColumn(
    "Previous_Close",
    lag("Close", 1).over(window_spec)
)

# daily return calculation
all_data = all_data.withColumn(
    "Daily_Return",
    (
        (col("Close") - col("Previous_Close"))
        / col("Previous_Close")
    ) * 100
)

# volatility calculation
volatility_window = window_spec.rowsBetween(-29, 0)

all_data = all_data.withColumn(
    "Volatility",
    stddev("Daily_Return").over(volatility_window)
)

# gain and loss calculation
all_data = all_data.withColumn(
    "Gain",
    when(col("Daily_Return") > 0, col("Daily_Return")).otherwise(0)
)

all_data = all_data.withColumn(
    "Loss",
    when(col("Daily_Return") < 0, -col("Daily_Return")).otherwise(0)
)

# 14 day window for RSI
rsi_window = window_spec.rowsBetween(-13, 0)

# average gain
all_data = all_data.withColumn(
    "Avg_Gain",
    avg("Gain").over(rsi_window)
)

# average loss
all_data = all_data.withColumn(
    "Avg_Loss",
    avg("Loss").over(rsi_window)
)

# relative strength
all_data = all_data.withColumn(
    "RS",
    col("Avg_Gain") / col("Avg_Loss")
)

# RSI calculation
all_data = all_data.withColumn(
    "RSI",
    100 - (100 / (1 + col("RS")))
)

# sharpe ratio calculation
all_data = all_data.withColumn(
    "Sharpe_Ratio",
    col("Daily_Return") / col("Volatility")
)

# show sample data
print("\nSample Data:\n")
all_data.select(
    "Date",
    "Stock",
    "Close",
    "RSI",
    "Sharpe_Ratio"
).show(10)

# save processed data
output_path = "data/processed_stock_data.parquet"

# convert spark dataframe into pandas
pandas_df = all_data.toPandas()

# save parquet file
pandas_df.to_parquet(
    output_path,
    index=False
)

print(f"\nProcessed data saved at: {output_path}")

# total rows
print(f"\nTotal rows: {all_data.count()}")