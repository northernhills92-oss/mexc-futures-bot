import streamlit as st
from data.market import get_usdt_pairs

st.title("🚀 MEXC Futures Bot Dashboard")

pairs = get_usdt_pairs()

st.write("Pairs found:", len(pairs))

if pairs:
    st.write("First 20 pairs:")
    st.write(pairs[:20])
else:
    st.error("No pairs found")
