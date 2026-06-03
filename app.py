import streamlit as st
from data.market import get_usdt_pairs, get_klines
from strategy.signal import score_signal

st.title("🚀 MEXC Futures Bot Dashboard")

pairs = get_usdt_pairs()

st.write("Pairs found:", len(pairs))

results = []

for symbol in pairs[:50]:
    try:
        df = get_klines(symbol)

        score = score_signal(df)

        results.append((symbol, score))

    except Exception as e:
        st.write(f"{symbol}: {e}")

if results:

    results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    best = results[0]

    st.subheader("🏆 Best Coin")

    st.write(best[0])
    st.write("Score:", best[1])

    st.subheader("Top 10")

    for row in results[:10]:
        st.write(row)

else:
    st.error("No valid results")
