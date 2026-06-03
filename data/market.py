import requests
import pandas as pd

BASE = "https://api.mexc.com"




def get_klines(symbol, interval="15m", limit=100):
    url = f"{BASE}/api/v3/klines"

    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }
def get_usdt_pairs():
    data = requests.get(
        f"{BASE}/api/v3/exchangeInfo"
    ).json()

    pairs = []

    for s in data["symbols"]:
        if s.get("quoteAsset") == "USDT":
            pairs.append(s["symbol"])

    return pairs
    data = requests.get(url, params=params).json()

    df = pd.DataFrame(
        data,
        columns=[
            "time","open","high","low","close","volume",
            "_1","_2","_3","_4","_5","_6"
        ]
    )

    numeric_cols = [
        "open","high","low","close","volume"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col])

    return df
