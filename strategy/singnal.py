def ema(series, span):
    return series.ewm(span=span).mean()


def rsi(series, period=14):
    delta = series.diff()
    gain = delta.clip(lower=0).rolling(period).mean()
    loss = (-delta.clip(upper=0)).rolling(period).mean()

    rs = gain / loss
    return 100 - (100 / (1 + rs))


def score_signal(df):
    close = df["close"]

    ema12 = ema(close, 12).iloc[-1]
    ema26 = ema(close, 26).iloc[-1]

    rsi_val = rsi(close).iloc[-1]

    score = 50

    # trend
    if ema12 > ema26:
        score += 30
    else:
        score -= 30

    # momentum
    if 45 <= rsi_val <= 65:
        score += 20
    else:
        score -= 20

    return score
