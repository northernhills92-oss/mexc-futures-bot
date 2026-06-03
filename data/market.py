import requests
import pandas as pd

BASE = "https://api.mexc.com"


def get_usdt_pairs():
    data = requests.get(
        f"{BASE}/api/v3/exchangeInfo",
        timeout=10
    ).json()

    pairs = []

    for s in data.get("symbols", []):
        if s.get("quoteAsset") == "USDT":
            pairs.append(s.get("symbol"))

    return pairs


def get_klines(symbol, interval="15m", limit=100):
    url = f"{BASE}/api/v3/klines"

    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }

    data = requests.get(url, params=params, timeout=10).json()

    if not isinstance(data, list):
        return pd.DataFrame()

    df = pd.DataFrame(data, columns=[
        "time","open","high","low","close","volume",
        "close_time","qv","trades","tb","tq","ignore"
    ])

    for col in ["open","high","low","close","volume"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df
