import sqlite3
import pandas as pd

# parquet file path
data_path = "data/processed_stock_data.parquet"

print("\nLoading processed stock data...\n")

# read parquet using pandas
df = pd.read_parquet(data_path)

print(df.head())

# create sqlite database
connection = sqlite3.connect("stock_market.db")

# save dataframe into database
df.to_sql(
    "stock_data",
    connection,
    if_exists="replace",
    index=False
)

print("\nDatabase created successfully!")

# sample query
query = """
SELECT Stock,
       AVG(Close) as Average_Close
FROM stock_data
GROUP BY Stock
"""

result = pd.read_sql(query, connection)

print("\nAverage Closing Prices:\n")
print(result)

# close connection
connection.close()