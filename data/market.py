import requests
import pandas as pd

BASE = "https://api.mexc.com"


def get_usdt_pairs():
    """
    Get all USDT trading pairs from MEXC Spot Exchange
    """

    try:
        response = requests.get(
            f"{BASE}/api/v3/exchangeInfo",
            timeout=10
        )

        data = response.json()

        pairs = []

        for s in data.get("symbols", []):

            if s.get("quoteAsset") == "USDT":
                pairs.append(s.get("symbol"))

        return pairs

    except Exception as e:
        print("get_usdt_pairs error:", e)
        return []


def get_klines(
    symbol,
    interval="15m",
    limit=100
):
    """
    Download candlestick data
    """

    try:

        url = f"{BASE}/api/v3/klines"

        params = {
            "symbol": symbol,
            "interval": interval,
            "limit": limit
        }

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        data = response.json()

        if not isinstance(data, list):
            return pd.DataFrame()

        if len(data) == 0:
            return pd.DataFrame()

        df = pd.DataFrame(
            data,
            columns=[
                "time",
                "open",
                "high",
                "low",
                "close",
                "volume",
                "close_time",
                "quote_volume",
                "trades",
                "taker_base",
                "taker_quote",
                "ignore"
            ]
        )

        numeric_cols = [
            "open",
            "high",
            "low",
            "close",
            "volume"
        ]

        for col in numeric_cols:
            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

        return df

    except Exception as e:
        print(f"get_klines error ({symbol}):", e)
        return pd.DataFrame()
