from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import GBTRegressor
from pyspark.ml.evaluation import RegressionEvaluator
import pandas as pd

# Spark Session

spark = SparkSession.builder \
    .appName("StockForecast") \
    .getOrCreate()

print("Loading data...")

# Read parquet using pandas

df = pd.read_parquet(
    "data/processed_stock_data.parquet"
)

# Remove datetime column
df = df.drop(columns=["Date"])

# Remove null values
df = df.dropna()

# Convert pandas to spark

data = spark.createDataFrame(df)

# Feature vector

assembler = VectorAssembler(
    inputCols=[
        "MA_7",
        "MA_30",
        "MA_90",
        "Volatility",
        "RSI"
    ],
    outputCol="features"
)

data = assembler.transform(data)

# Train-test split

train_data, test_data = data.randomSplit(
    [0.8, 0.2],
    seed=42
)

# Model

gbt = GBTRegressor(
    featuresCol="features",
    labelCol="Close",
    maxIter=10
)

print("Training model...")

model = gbt.fit(train_data)

# Prediction

predictions = model.transform(test_data)

# Evaluation

evaluator = RegressionEvaluator(
    labelCol="Close",
    predictionCol="prediction",
    metricName="rmse"
)

rmse = evaluator.evaluate(predictions)

print(f"RMSE: {rmse}")

# Save model

# model.write().overwrite().save(
#     "ml_models/gbt_forecasting_model"
# )

print("GBT forecasting model saved successfully.")

spark.stop()