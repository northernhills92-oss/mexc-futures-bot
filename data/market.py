import requests
import pandas as pd

BASE = "https://api.mexc.com"

def get_usdt_pairs():

    response = requests.get(
        f"{BASE}/api/v3/exchangeInfo",
        timeout=10
    )

    data = response.json()

    print("SYMBOL COUNT =", len(data.get("symbols", [])))

    if len(data.get("symbols", [])) > 0:
        print("FIRST SYMBOL =", data["symbols"][0])

    pairs = []

    for s in data.get("symbols", []):

        if s.get("quoteAsset") == "USDT":
            pairs.append(s.get("symbol"))

    print("USDT COUNT =", len(pairs))

    return pairs
