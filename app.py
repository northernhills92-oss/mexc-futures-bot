import streamlit as st
from data.market import get_usdt_pairs, get_klines
from strategy.signal import score_signal

st.title(" MEXC Futures Bot Dashboard")

pairs = get_usdt_pairs()

st.write("Pairs found:", len(pairs))

results = []

for symbol in pairs[:10]:
    try:
        df = get_klines(symbol)
        score = score_signal(df)
        results.append((symbol, score))
    except Exception as e:
        st.write(f"Error {symbol}: {e}")

st.write("Results count:", len(results))

if len(results) > 0:
    results.sort(key=lambda x: x[1], reverse=True)

    best = results[0]

    st.subheader(" Best Trade Candidate")
    st.write(best)
else:
    st.error("No valid results found.")
