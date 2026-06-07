import joblib
import pandas as pd

# load trained model
model = joblib.load(
    "ml_models/stock_prediction_model.pkl"
)

print("\nStock Trend Prediction\n")

# user input
ma7 = float(input("Enter MA_7: "))
ma30 = float(input("Enter MA_30: "))
ma90 = float(input("Enter MA_90: "))
volatility = float(input("Enter Volatility: "))
rsi = float(input("Enter RSI: "))

# create dataframe
input_data = pd.DataFrame({
    "MA_7": [ma7],
    "MA_30": [ma30],
    "MA_90": [ma90],
    "Volatility": [volatility],
    "RSI": [rsi]
})

# prediction
prediction = model.predict(input_data)

# result
if prediction[0] == 1:
    print("\nPrediction: Stock price may go UP")
else:
    print("\nPrediction: Stock price may go DOWN")