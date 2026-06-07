import yfinance as yf
import pandas as pd
import os
import time

stock_list = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]

start = "2020-01-01"
end = "2026-01-01"

output_folder = "data/stock_data"

os.makedirs(output_folder, exist_ok=True)

print("\nDownloading stock market data...\n")

for stock in stock_list:

    print(f"Fetching data for {stock}...")

    try:
        # create ticker object
        ticker = yf.Ticker(stock)

        # get historical data
        stock_data = ticker.history(
            start=start,
            end=end
        )

        # check if data exists
        if stock_data.empty:
            print(f"No data found for {stock}\n")
            continue

        stock_data.reset_index(inplace=True)

        save_path = f"{output_folder}/{stock}_stock_data.csv"

        stock_data.to_csv(save_path, index=False)

        print(f"{stock} data saved successfully")
        print(f"Total rows: {len(stock_data)}\n")

        # small delay to avoid request blocking
        time.sleep(2)

    except Exception as error:
        print(f"Problem downloading {stock}")
        print(error)

print("All stock data downloaded.")