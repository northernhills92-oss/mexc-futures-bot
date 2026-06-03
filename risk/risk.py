def risk_ok(balance, start_balance):
    change = (balance - start_balance) / start_balance
    return change > -0.03


def position_size(balance, risk_pct, entry, sl):
    risk_amount = balance * risk_pct
    distance = abs(entry - sl)

    if distance == 0:
        return 0

    return risk_amount / distance
