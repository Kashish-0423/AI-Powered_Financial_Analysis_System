import os
import joblib
import pandas as pd


def test_processed_data_exists():

    assert os.path.exists(
        "data/processed_stock_data.parquet"
    )


def test_processed_data_not_empty():

    data = pd.read_parquet(
        "data/processed_stock_data.parquet"
    )

    assert len(data) > 0


def test_required_columns():

    data = pd.read_parquet(
        "data/processed_stock_data.parquet"
    )

    required_columns = [

        "Stock",
        "Date",
        "Close",
        "MA_7",
        "MA_30",
        "MA_90",
        "RSI",
        "Volatility",
        "Sharpe_Ratio"

    ]

    for column in required_columns:

        assert column in data.columns


def test_model_exists():

    assert os.path.exists(
        "ml_models/stock_prediction_model.pkl"
    )


def test_model_prediction():

    model = joblib.load(
        "ml_models/stock_prediction_model.pkl"
    )

    sample = pd.DataFrame({

        "MA_7": [100],
        "MA_30": [98],
        "MA_90": [95],
        "Volatility": [0.02],
        "RSI": [60]

    })

    prediction = model.predict(
        sample
    )

    assert prediction[0] in [0, 1]


def test_prediction_probability():

    model = joblib.load(
        "ml_models/stock_prediction_model.pkl"
    )

    sample = pd.DataFrame({

        "MA_7": [100],
        "MA_30": [98],
        "MA_90": [95],
        "Volatility": [0.02],
        "RSI": [60]

    })

    probability = model.predict_proba(
        sample
    )[0]

    assert len(
        probability
    ) == 2


def test_database_exists():

    assert os.path.exists(
        "stock_market.db"
    )