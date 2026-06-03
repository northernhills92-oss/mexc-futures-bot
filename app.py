import requests
import streamlit as st

data = requests.get(
    "https://api.mexc.com/api/v3/exchangeInfo"
).json()

usdt_pairs = []

for s in data["symbols"]:
    if s.get("quoteAsset") == "USDT":
        usdt_pairs.append(s["symbol"])

st.write("USDT pairs:", len(usdt_pairs))
st.write(usdt_pairs[:20])
