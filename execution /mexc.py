import requests

BASE = "https://contract.mexc.com"


def place_order(symbol, side, volume, leverage):
    url = BASE + "/api/v1/private/order/submit"

    data = {
        "symbol": symbol,
        "side": side,
        "vol": volume,
        "leverage": leverage,
        "type": 1
    }

    try:
        res = requests.post(url, json=data)
        return res.json()
    except Exception as e:
        print("Order error:", e)
        return None
