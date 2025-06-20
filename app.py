import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("price_predictor.pkl")

# App Title
st.title("📊 Stock Price Predictor")
st.subheader("Enter today's stock data to get the predicted closing price for tomorrow")

# Input fields
open_price = st.number_input("Open Price", min_value=0.0, format="%.2f")
high_price = st.number_input("High Price", min_value=0.0, format="%.2f")
low_price = st.number_input("Low Price", min_value=0.0, format="%.2f")
close_price = st.number_input("Close Price", min_value=0.0, format="%.2f")
volume = st.number_input("Volume", min_value=0)

# Predict button
if st.button("Predict"):
    input_data = pd.DataFrame([{
        "Open": open_price,
        "High": high_price,
        "Low": low_price,
        "Close": close_price,
        "Volume": volume
    }])
    
    predicted_price = model.predict(input_data)[0]

    # Display prediction
    st.success(f"📈 Predicted Next-Day Closing Price: ₹{predicted_price:.2f}")

    # Recommendation logic
    if predicted_price > close_price * 1.01:
        advice = "Buy 📈"
    elif predicted_price < close_price * 0.99:
        advice = "Sell 📉"
    else:
        advice = "Hold 🤝"

    # Show recommendation
    st.info(f"💡 Recommendation: {advice}")
