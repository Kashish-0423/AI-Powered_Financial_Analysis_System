from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI(
    title="Stock Prediction API"
)

model = joblib.load(
    "ml_models/stock_prediction_model.pkl"
)

@app.get("/")
def home():

    return {
        "message": "Stock Prediction API Running"
    }

@app.post("/predict")
def predict(
    ma7: float,
    ma30: float,
    ma90: float,
    volatility: float,
    rsi: float
):

    input_data = pd.DataFrame({

        "MA_7": [ma7],
        "MA_30": [ma30],
        "MA_90": [ma90],
        "Volatility": [volatility],
        "RSI": [rsi]

    })

    prediction = model.predict(
        input_data
    )[0]

    probability = model.predict_proba(
        input_data
    )[0]

    return {

        "prediction": int(prediction),
        "up_probability": float(probability[1]),
        "down_probability": float(probability[0])

    }