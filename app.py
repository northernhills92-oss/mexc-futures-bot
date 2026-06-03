import streamlit as st
import requests

url = "https://api.mexc.com/api/v3/exchangeInfo"

data = requests.get(url).json()

st.write("Symbols count:", len(data["symbols"]))

st.write(data["symbols"][0])
