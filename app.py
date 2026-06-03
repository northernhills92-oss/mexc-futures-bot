import streamlit as st
from data.market import get_klines

st.title("🚀 Kline Test")

df = get_klines("BTCUSDT")

st.write("Rows:", len(df))

st.dataframe(df.tail())
