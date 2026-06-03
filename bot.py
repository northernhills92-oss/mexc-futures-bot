import time

from data.market import get_usdt_pairs, get_klines
from strategy.signal import score_signal
from config import SCORE_THRESHOLD


open_position = None
start_balance = 1000
balance = start_balance


while True:

    try:
        pairs = get_usdt_pairs()
        results = []

        for symbol in pairs:
            df = get_klines(symbol, "15m")
            score = score_signal(df)

            results.append((symbol, score))

        results.sort(key=lambda x: x[1], reverse=True)

        best_symbol, best_score = results[0]

        print("BEST:", best_symbol, best_score)

        # 1 trade only logic
        if best_score >= SCORE_THRESHOLD and open_position is None:
            print("TRADE SIGNAL:", best_symbol)

            # TODO: place real order later
            open_position = best_symbol

        time.sleep(60)

    except Exception as e:
        print("Error:", e)
        time.sleep(10)
