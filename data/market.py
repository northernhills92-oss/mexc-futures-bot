import requests
import pandas as pd

BASE = "https://api.mexc.com"


def get_usdt_pairs():
    try:
        r = requests.get(f"{BASE}/api/v3/exchangeInfo", timeout=10)
        data = r.json()

        pairs = []

        for s in data.get("symbols", []):
            if s.get("quoteAsset") == "USDT":
                pairs.append(s.get("symbol"))

        return pairs

    except Exception as e:
        print("get_usdt_pairs error:", e)
        return []


def get_klines(symbol, interval="15m", limit=100):
    try:
        url = f"{BASE}/api/v3/klines"

        params = {
            "symbol": symbol,
            "interval": interval,
            "limit": limit
        }

        r = requests.get(url, params=params, timeout=10)
        data = r.json()

        if not isinstance(data, list):
            return pd.DataFrame()

        df = pd.DataFrame(
            data,
            columns=[
                "time","open","high","low","close","volume",
                "close_time","qv","trades","tb","tq","ignore"
            ]
        )

        for col in ["open","high","low","close","volume"]:
            df[col] = pd.to_numeric(df[col], errors="coerce")

        return df

    except Exception as e:
        print("get_klines error:", e)
        return pd.DataFrame()
