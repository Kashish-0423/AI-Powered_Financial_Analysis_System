import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)
import streamlit as st
import pandas as pd
import joblib

from chatbot.ai_prediction_chatbot import AIPredictionChatbot

# Page settings
st.set_page_config(
    page_title="Stock Market Dashboard",
    layout="wide"
)

# Title
st.title("📈 AI Stock Market Analysis Dashboard")

st.markdown(
    "Analyze stock trends, technical indicators and predict future movement."
)

# Load dataset
data = pd.read_parquet(
    "data/processed_stock_data.parquet"
)

# Load model
model = joblib.load(
    "ml_models/stock_prediction_model.pkl"
)

# Initialize chatbot
chatbot = AIPredictionChatbot()

# Sidebar
st.sidebar.title("Dashboard Controls")

companies = sorted(data["Stock"].unique())

selected_company = st.sidebar.selectbox(
    "Select Company",
    companies
)

# Filter data
company_data = data[data["Stock"] == selected_company].sort_values("Date")
company_data["Date"] = pd.to_datetime(company_data["Date"])

latest_row = company_data.iloc[-1]

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Current Price", f"${latest_row['Close']:.2f}")

with col2:
    st.metric("RSI", f"{latest_row['RSI']:.2f}")

with col3:
    st.metric("Volatility", f"{latest_row['Volatility']:.2f}")

st.markdown("---")

# Data Preview
st.subheader(f"{selected_company} Stock Data")

st.dataframe(
    company_data.tail(10),
    use_container_width=True
)

st.markdown("---")

# Charts
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("Closing Price Trend")
    st.line_chart(
        company_data.set_index("Date")[["Close", "MA_7", "MA_30", "MA_90"]]
    )

with chart_col2:
    st.subheader("RSI Trend")
    st.line_chart(
        company_data.set_index("Date")[["RSI"]]
    )

st.markdown("---")

# Statistics
st.subheader("Company Statistics")

stats_col1, stats_col2, stats_col3 = st.columns(3)

with stats_col1:
    st.write(f"Average Closing Price: ${company_data['Close'].mean():.2f}")

with stats_col2:
    st.write(f"Highest Price: ${company_data['Close'].max():.2f}")

with stats_col3:
    st.write(f"Lowest Price: ${company_data['Close'].min():.2f}")

st.markdown("---")

# Prediction Section
st.subheader("🔮 Predict Stock Movement")

input_col1, input_col2 = st.columns(2)

with input_col1:
    ma7 = st.number_input("MA_7", value=float(latest_row["MA_7"]))
    ma30 = st.number_input("MA_30", value=float(latest_row["MA_30"]))
    ma90 = st.number_input("MA_90", value=float(latest_row["MA_90"]))

with input_col2:
    volatility = st.number_input("Volatility", value=float(latest_row["Volatility"]))
    rsi = st.number_input("RSI", value=float(latest_row["RSI"]))

if st.button("Predict Trend"):

    input_data = pd.DataFrame({
        "MA_7": [ma7],
        "MA_30": [ma30],
        "MA_90": [ma90],
        "Volatility": [volatility],
        "RSI": [rsi]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("📈 Prediction Result: Stock price may increase.")
        st.info("Market indicators show a possible upward trend.")
    else:
        st.error("📉 Prediction Result: Stock price may decrease.")
        st.warning("Market indicators show a possible downward trend.")

    probability = model.predict_proba(input_data)[0]

    st.subheader("Prediction Confidence")
    st.write(f"📈 Up Probability: {probability[1]*100:.2f}%")
    st.write(f"📉 Down Probability: {probability[0]*100:.2f}%")

st.markdown("---")

# Investment Classification
st.subheader("Investment Classification")

score = 0

if latest_row["RSI"] < 70:
    score += 3

if latest_row["Sharpe_Ratio"] > 0:
    score += 3

if latest_row["MA_7"] > latest_row["MA_30"]:
    score += 4

if score >= 7:
    st.success("High Investment Potential")
elif score >= 4:
    st.warning("Medium Investment Potential")
else:
    st.error("Low Investment Potential")

st.write(f"Investment Score: {score}/10")

st.markdown("---")

# =========================
# 🤖 AI ASSISTANT (OLLAMA)
# =========================

st.subheader("🤖 AI Stock Assistant")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_question = st.text_input("Ask a finance related question")

if user_question:

    response = chatbot.answer_question(user_question)

    st.session_state.chat_history.append({
        "user": user_question,
        "ai": response
    })

# Display chat history
for chat in reversed(st.session_state.chat_history):

    st.markdown(f"**🧑 You:** {chat['user']}")
    st.markdown(f"**🤖 AI:** {chat['ai']}")
    st.markdown("---")

st.markdown("---")

st.caption("Built using Machine Learning, Ollama LLM and Streamlit")