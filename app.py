import streamlit as st
import requests

url = "https://api.mexc.com/api/v3/exchangeInfo"

try:
    r = requests.get(url, timeout=10)

    st.write("Status:", r.status_code)

    data = r.json()

    st.write("Symbols count:", len(data.get("symbols", [])))

    if len(data.get("symbols", [])) > 0:
        st.write("First symbol:")
        st.json(data["symbols"][0])

except Exception as e:
    st.error(str(e))
