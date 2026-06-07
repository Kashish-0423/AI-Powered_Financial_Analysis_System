# AI-Powered Financial Analysis Platform

## Setup Guide

### System Requirements

Before running the project, ensure the following software is installed:

- Python 3.10 or above
- Java 8 or Java 11 (Required for PySpark)
- Ollama
- Git (Optional)

---

## Step 1: Download the Project

Download or clone the project and extract it to your desired location.

Project Structure:

```text
Sabudh Project/
│
├── api/
├── chatbot/
├── config/
├── dashboard/
├── data/
├── data_collection/
├── forecasting/
├── ml_models/
├── preprocessing/
├── sql_interface/
├── tests/
│
├── main.py
├── requirements.txt
├── stock_market.db
└── README.md
```

---

## Step 2: Create Virtual Environment

Open Command Prompt inside the project folder.

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

```bash
venv\Scripts\activate
```

After activation, you should see:

```bash
(venv)
```

at the beginning of the terminal line.

---

## Step 3: Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

Verify installation:

```bash
pip list
```

---

## Step 4: Configure Java for PySpark

Verify Java installation:

```bash
java -version
```

Expected output:

```text
java version "11.x.x"
```

If Java is not installed, install OpenJDK 11.

---

## Step 5: Install Ollama

Download Ollama from:

https://ollama.com/download

Install Ollama and verify installation:

```bash
ollama --version
```

---

## Step 6: Download Llama 3.2 Model

The AI chatbot uses the Llama 3.2 model.

Run:

```bash
ollama pull llama3.2
```

Verify model installation:

```bash
ollama list
```

Expected output:

```text
NAME
llama3.2
```

---

## Step 7: Start Ollama

Before running the chatbot, start the Ollama service:

```bash
ollama serve
```

Keep this terminal window open.

Open another terminal for running the project.

---

## Step 8: Run the Project

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Run:

```bash
python main.py
```

The following menu will appear:

```text
========== AI Financial Analysis Platform ==========

1. Data Collection
2. Data Preprocessing
3. Database Setup
4. Train ML Models
5. Run API
6. Run Dashboard
7. Exit
```

Select the required option.

---

## Step 9: Run Dashboard Directly

The Streamlit dashboard can also be launched directly:

```bash
python -m streamlit run dashboard/app.py
```

Dashboard URL:

```text
http://localhost:8501
```

---

## Step 10: Run FastAPI Server

To start the API manually:

```bash
python -m uvicorn api.app:app --reload
```

API URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Step 11: Run Tests

Execute all tests:

```bash
pytest tests -v
```

Expected output:

```text
7 passed
```

---

# Common Issues

## PySpark Error

Problem:

```text
HADOOP_HOME and hadoop.home.dir are unset
```

Solution:

Install Hadoop utilities and configure the required environment variables.

---

## Ollama Connection Error

Problem:

```text
Connection refused
```

Solution:

Ensure Ollama is running:

```bash
ollama serve
```

---

## Module Import Error

Problem:

```text
ModuleNotFoundError
```

Solution:

Run commands from the project root directory and ensure the virtual environment is activated.

---

## Streamlit Error

Problem:

```text
'streamlit' is not recognized
```

Solution:

Install Streamlit:

```bash
pip install streamlit
```

or run:

```bash
python -m streamlit run dashboard/app.py
```

---

# Project Features

- Stock Data Collection using Yahoo Finance
- Data Processing using PySpark
- Feature Engineering
- SQLite Database Storage
- Machine Learning Predictions
- FastAPI Integration
- Streamlit Dashboard
- Investment Classification
- Ollama-Powered AI Chatbot
- Automated Testing

---

# Author

**Kashish**

AI-Powered Financial Analysis Platform