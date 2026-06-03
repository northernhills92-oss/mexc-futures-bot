import requests
import pandas as pd

BASE = "https://api.mexc.com"

def get_usdt_pairs():
    url = f"{BASE}/api/v3/exchangeInfo"

    data = requests.get(url).json()

    pairs = []

    for s in data["symbols"]:
        symbol = s.get("symbol", "")

        if symbol.endswith("USDT"):
            pairs.append(symbol)

    return pairs
