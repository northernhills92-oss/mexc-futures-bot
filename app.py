import streamlit as st
from data.market import get_usdt_pairs, get_klines
from strategy.signal import score_signal

st.title("🚀 MEXC Futures Bot Dashboard")

try:
    pairs = get_usdt_pairs()

    st.write("Pairs found:", len(pairs))

    if len(pairs) > 0:
        st.write("First 10 pairs:")
        st.write(pairs[:10])

    results = []

    # Speed အတွက် 50 ခုပဲ scan
    for symbol in pairs[:50]:
        try:
            df = get_klines(symbol)

            if len(df) == 0:
                continue

            score = score_signal(df)

            results.append({
                "symbol": symbol,
                "score": score
            })

        except Exception as e:
            st.write(f"Error on {symbol}: {e}")

    st.write("Valid results:", len(results))

    if len(results) > 0:

        results = sorted(
            results,
            key=lambda x: x["score"],
            reverse=True
        )

        best = results[0]

        st.subheader("🏆 Best Coin")
        st.write(best["symbol"])
        st.write("Score:", best["score"])

        st.subheader("📊 Top 10 Coins")

        for row in results[:10]:
            st.write(
                f"{row['symbol']} | Score: {row['score']}"
            )

    else:
        st.error("No valid results")

except Exception as e:
    st.error(f"App Error: {e}")
