import streamlit as st
from data import market

st.title("DEBUG")

st.write("Market module:", market.__file__)

pairs = market.get_usdt_pairs()

st.write("Pairs found:", len(pairs))

if pairs:
    st.write(pairs[:10])
