import joblib
import pandas as pd
import ollama

from chatbot.investment_chatbot import InvestmentChatbot


class AIPredictionChatbot:

    def __init__(self):

        self.database = InvestmentChatbot()

        self.model = joblib.load(
            "ml_models/stock_prediction_model.pkl"
        )

        self.tickers = [
            "AAPL",
            "MSFT",
            "GOOGL",
            "AMZN",
            "TSLA"
        ]

    def predict_stock(
        self,
        ma7,
        ma30,
        ma90,
        volatility,
        rsi
    ):

        input_data = pd.DataFrame({

            "MA_7": [ma7],
            "MA_30": [ma30],
            "MA_90": [ma90],
            "Volatility": [volatility],
            "RSI": [rsi]

        })

        prediction = self.model.predict(
            input_data
        )[0]

        probability = self.model.predict_proba(
            input_data
        )[0]

        return {

            "prediction": int(prediction),

            "up_probability":
                float(probability[1]),

            "down_probability":
                float(probability[0])

        }

    def answer_question(
        self,
        question
    ):

        q = question.lower()

        # ------------------------
        # Stock Data Queries
        # ------------------------

        for ticker in self.tickers:

            if ticker.lower() in q:

                # Show stock data

                if (
                    "show" in q
                    or "data" in q
                    or "history" in q
                ):

                    data = self.database.get_stock_data(
                        ticker,
                        5
                    )

                    if data.empty:
                        return (
                            f"No data found for {ticker}"
                        )

                    return (
                        f"Latest 5 records for {ticker}:\n\n"
                        + data.to_string(
                            index=False
                        )
                    )

                # Tell me about stock

                if (
                    "tell me about" in q
                    or "summary" in q
                    or "about" in q
                ):

                    stock = (
                        self.database
                        .get_latest_stock_summary(
                            ticker
                        )
                    )

                    if stock is None:
                        return (
                            f"No data available for {ticker}"
                        )

                    return f"""
Stock: {ticker}

Current Close Price: {stock['Close']}

RSI: {stock['RSI']:.2f}

Volatility: {stock['Volatility']:.4f}

MA_7: {stock['MA_7']:.2f}

MA_30: {stock['MA_30']:.2f}

Sharpe Ratio: {stock['Sharpe_Ratio']:.2f}
"""

                # Prediction

                if "predict" in q:

                    stock = (
                        self.database
                        .get_latest_stock_summary(
                            ticker
                        )
                    )

                    if stock is None:
                        return (
                            f"No data available for {ticker}"
                        )

                    result = self.predict_stock(

                        stock["MA_7"],
                        stock["MA_30"],
                        stock["MA_90"],
                        stock["Volatility"],
                        stock["RSI"]

                    )

                    direction = (
                        "UP 📈"
                        if result["prediction"] == 1
                        else "DOWN 📉"
                    )

                    return f"""
Prediction for {ticker}

Direction: {direction}

Up Probability:
{result['up_probability']*100:.2f}%

Down Probability:
{result['down_probability']*100:.2f}%
"""

        # ------------------------
        # Technical Questions
        # ------------------------

        if "rsi" in q:

            return (
                "RSI (Relative Strength Index) measures "
                "whether a stock is overbought or oversold."
            )

        elif "moving average" in q:

            return (
                "Moving averages help identify "
                "the direction of stock trends."
            )

        elif "volatility" in q:

            return (
                "Volatility measures how much "
                "a stock price fluctuates."
            )

        elif "sharpe" in q:

            return (
                "Sharpe Ratio measures risk-adjusted return."
            )

        # ------------------------
        # Ollama Fallback
        # ------------------------

        try:

            response = ollama.chat(

                model="llama3.2",

                messages=[
                    {
                        "role": "user",
                        "content": question
                    }
                ]

            )

            return response[
                "message"
            ][
                "content"
            ]

        except Exception as e:

            return (
                "Ollama Error:\n"
                f"{str(e)}"
            )