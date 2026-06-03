import streamlit as st
import requests

st.title("🚀 MEXC Futures Bot Dashboard")

data = requests.get(
    "https://api.mexc.com/api/v3/exchangeInfo"
).json()

pairs = []

for s in data["symbols"]:
    if s.get("quoteAsset") == "USDT":
        pairs.append(s["symbol"])

st.write("Pairs found:", len(pairs))
st.write("First 20 pairs:")
st.write(pairs[:20])
