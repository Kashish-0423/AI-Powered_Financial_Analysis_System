import pandas as pd

# load stock dataset
data = pd.read_parquet(
    "data/processed_stock_data.parquet"
)

print("\nAI Stock Assistant")
print("Type 'exit' to stop chatbot.\n")

while True:

    user_input = input("Ask something: ").lower()

    # exit condition
    if user_input == "exit":
        print("Chatbot stopped.")
        break

    # RSI
    elif "rsi" in user_input:
        print("\nRSI measures whether a stock is overbought or oversold.\n")

    # volatility
    elif "volatility" in user_input:
        highest_volatility = data.groupby("Stock")[
            "Volatility"
        ].mean().idxmax()

        print(
            f"\n{highest_volatility} has the highest average volatility.\n"
        )

    # sharpe ratio
    elif "sharpe" in user_input:
        print(
            "\nSharpe Ratio measures return compared to risk.\n"
        )

    # moving average
    elif "moving average" in user_input:
        print(
            "\nMoving averages help identify stock trends.\n"
        )

    # stock price
    elif "highest price" in user_input:

        highest_stock = data.loc[
            data["Close"].idxmax()
        ]

        print(
            f"\nHighest stock price was for "
            f"{highest_stock['Stock']}"
        )

    # default response
    else:
        print(
            "\nSorry, I don't understand that question.\n"
        )