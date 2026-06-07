import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import joblib

# load data
data = pd.read_parquet(
    "data/processed_stock_data.parquet"
)

print("\nDataset Loaded\n")

# create target
# next day's movement

data["Target"] = (
    data.groupby("Stock")["Close"]
    .shift(-1)
    > data["Close"]
).astype(int)

# remove null values
data = data.dropna()

# features
features = [
    "MA_7",
    "MA_30",
    "MA_90",
    "Volatility",
    "RSI"
]

X = data[features]

y = data["Target"]

print("Target Distribution:\n")
print(y.value_counts())

# time based split

split_index = int(
    len(data) * 0.8
)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

print("\nTraining model...\n")

# model

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=8,
    random_state=42,
    class_weight="balanced"
)

# train

model.fit(
    X_train,
    y_train
)

# prediction

predictions = model.predict(
    X_test
)

# accuracy

accuracy = accuracy_score(
    y_test,
    predictions
)

print(
    f"\nModel Accuracy: {accuracy:.2f}\n"
)

print(
    classification_report(
        y_test,
        predictions
    )
)

# save model

joblib.dump(
    model,
    "ml_models/stock_prediction_model.pkl"
)

print(
    "\nModel saved successfully!"
)