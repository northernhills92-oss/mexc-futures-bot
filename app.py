import streamlit as st
from data.market import get_usdt_pairs

pairs = get_usdt_pairs()

st.write("Pairs found:", len(pairs))
