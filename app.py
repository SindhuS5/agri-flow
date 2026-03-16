import streamlit as st
import pandas as pd

# Title & Language Selection
st.title("🌱 AgriFlow: Farmer Assistant")
lang = st.selectbox("Select Language", ["English", "తెలుగు", "हिन्दी"])

# 1. Digital Ledger
st.header("💰 Expense Tracker")
cost = st.number_input("Enter Input Cost (Seeds/Labor)", min_value=0)
expected_price = st.number_input("Expected Selling Price", min_value=0)

if st.button("Calculate Profit"):
    profit = expected_price - cost
    st.success(f"Projected Profit: ₹{profit}")

# 2. Cold Storage Map (Mock Data)
st.header("📍 Nearby Cold Storage")
map_data = pd.DataFrame({'lat': [13.62], 'lon': [78.50]}) # Madanapalle area
st.map(map_data)
