import requests
import pandas as pd

BASE = "https://api.mexc.com"

def get_usdt_pairs():
    r = requests.get(f"{BASE}/api/v3/exchangeInfo", timeout=10)
    data = r.json()

    return [
        s.get("symbol")
        for s in data.get("symbols", [])
        if s.get("quoteAsset") == "USDT"
    ]


def get_klines(symbol, interval="15m", limit=100):
    r = requests.get(
        f"{BASE}/api/v3/klines",
        params={
            "symbol": symbol,
            "interval": interval,
            "limit": limit
        },
        timeout=10
    )

    data = r.json()

    if not isinstance(data, list):
        return pd.DataFrame()

    df = pd.DataFrame(data, columns=[
        "time","open","high","low","close","volume",
        "ct","qv","trades","tb","tq","ignore"
    ])

    for c in ["open","high","low","close","volume"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    return df
