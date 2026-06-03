import requests
import pandas as pd

BASE_URL = "https://api.mexc.com"


def get_usdt_pairs():
    url = f"{BASE_URL}/api/v3/exchangeInfo"
    data = requests.get(url).json()

    pairs = []
    for s in data["symbols"]:
        if s["symbol"].endswith("USDT") and s["status"] == "ENABLED":
            pairs.append(s["symbol"])

    return pairs


def get_klines(symbol, interval="15m", limit=100):
    url = f"{BASE_URL}/api/v3/klines"
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }

    data = requests.get(url, params=params).json()

    df = pd.DataFrame(data, columns=[
        "time","open","high","low","close","volume",
        "_1","_2","_3","_4","_5","_6"
    ])

    df = df.astype(float)
    return df
