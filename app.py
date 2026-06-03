import streamlit as st
import requests

url = "https://api.mexc.com/api/v3/exchangeInfo"

r = requests.get(url)

st.write("Status:", r.status_code)

data = r.json()

st.write(data)
