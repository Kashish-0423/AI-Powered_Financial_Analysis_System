def stock_chatbot(question):

    question = question.lower()

    if "rsi" in question:
        return "RSI indicates whether a stock is overbought or oversold."

    elif "moving average" in question:
        return "Moving averages help identify trends."

    elif "volatility" in question:
        return "Volatility measures price fluctuations."

    elif "sharpe" in question:
        return "Sharpe Ratio compares return with investment risk."

    elif "buy" in question:
        return "Investment decisions should consider multiple indicators."

    else:
        return "Sorry, I do not understand the question."


if __name__ == "__main__":

    print("AI Stock Assistant")

    while True:

        q = input("Question: ")

        if q.lower() == "exit":
            break

        print(stock_chatbot(q))