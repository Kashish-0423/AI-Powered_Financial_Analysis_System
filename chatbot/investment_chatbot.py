import sqlite3
import pandas as pd


class InvestmentChatbot:

    def __init__(self):

        self.connection = sqlite3.connect(
            "stock_market.db"
        )

    def get_stock_data(
        self,
        ticker,
        days=10
    ):

        try:

            query = f"""
            SELECT *
            FROM stock_data
            WHERE Stock='{ticker}'
            ORDER BY Date DESC
            LIMIT {days}
            """

            data = pd.read_sql(
                query,
                self.connection
            )

            return data

        except Exception as e:

            return pd.DataFrame(
                {"Error": [str(e)]}
            )

    def get_latest_stock_summary(
        self,
        ticker
    ):

        try:

            query = f"""
            SELECT *
            FROM stock_data
            WHERE Stock='{ticker}'
            ORDER BY Date DESC
            LIMIT 1
            """

            data = pd.read_sql(
                query,
                self.connection
            )

            if data.empty:
                return None

            return data.iloc[0]

        except:
            return None

    def close(self):

        self.connection.close()