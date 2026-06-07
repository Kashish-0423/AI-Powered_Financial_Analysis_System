# 📈 AI-Powered Financial Analysis Platform

## Project Overview

This project is an AI-Powered Financial Analysis Platform developed using PySpark, Machine Learning, FastAPI, and Streamlit.

The system collects stock market data, performs feature engineering, trains machine learning models, provides stock movement predictions, offers investment classification, and displays results through an interactive dashboard.

---

## Features

### ✅ Data Collection

* Download historical stock data
* Multiple company support
* CSV data storage

### ✅ Data Preprocessing

* PySpark-based processing
* Moving Averages (MA_7, MA_30, MA_90)
* RSI Calculation
* Daily Return
* Volatility
* Sharpe Ratio

### ✅ Database

* SQLite database integration
* Historical stock data storage
* Fast data retrieval

### ✅ Machine Learning

* Stock movement prediction model
* Investment classification
* Prediction probabilities

### ✅ FastAPI

* REST API for predictions
* JSON output
* Easy integration

Example Response:

```json
{
    "prediction": 1,
    "up_probability": 0.53,
    "down_probability": 0.47
}
```

### ✅ Streamlit Dashboard

Dashboard includes:

* Historical stock data
* Price trend visualization
* Moving Average charts
* RSI chart
* Company statistics
* Stock prediction
* Investment classification
* AI Finance Assistant

### ✅ AI Chatbot

The chatbot can answer questions related to:

* RSI
* Moving Average
* Volatility
* Sharpe Ratio
* Daily Return
* Stock Predictions

---

# Tech Stack

* Python
* PySpark
* Pandas
* SQLite
* Scikit-Learn
* Joblib
* FastAPI
* Streamlit
* Matplotlib
* Pytest

---

# Project Structure

```
Sabudh Project/

│
├── api/
│   └── app.py
│
├── chatbot/
│   ├── investment_chatbot.py
│   └── ai_prediction_chatbot.py
│
├── dashboard/
│   └── app.py
│
├── data/
│   └── processed_stock_data.parquet
│
├── ml_models/
│   └── stock_prediction_model.pkl
│
├── tests/
│   └── test_pipeline.py
│
├── stock_market.db
│
└── README.md
```

---

# Machine Learning Features

The prediction model uses:

* MA_7
* MA_30
* MA_90
* RSI
* Volatility

The investment classification uses:

* RSI
* Sharpe Ratio
* Moving Average Trend

---

# How to Run

## Step 1

Activate virtual environment

```
venv\Scripts\activate
```

---

## Step 2

Run FastAPI

```
python -m uvicorn api.app:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## Step 3

Run Streamlit Dashboard

```
streamlit run dashboard/app.py
```

Open:

```
http://localhost:8501
```

---

## API Testing

Example Input:

```json
{
    "MA_7": 100,
    "MA_30": 98,
    "MA_90": 95,
    "Volatility": 0.02,
    "RSI": 60
}
```

Example Output:

```json
{
    "prediction": 1,
    "up_probability": 0.53,
    "down_probability": 0.47
}
```

---

# Testing

Unit tests were created using Pytest.

Run tests:

```
pytest tests/test_pipeline.py -v
```

Result:

```
7 passed
```

Test Coverage:

* Data availability
* Required columns
* ML model existence
* Prediction generation
* Prediction probability
* Database availability

---

# Dashboard Modules

* Stock Data Viewer
* Technical Indicators
* Prediction System
* Investment Classification
* AI Assistant

---

# Future Improvements

* Ollama LLM Integration
* Advanced AI Chatbot
* Real-time Stock Data
* Deep Learning Models
* Cloud Deployment

---

# Conclusion

This project demonstrates a complete Data Engineering and Machine Learning pipeline for financial analytics. It combines data processing, predictive modeling, API development, dashboard visualization, and AI-based interaction into a single platform.

---

## Author

**Kashish**

AI-Powered Financial Analysis Platform

Built using PySpark, Machine Learning, FastAPI and Streamlit.
