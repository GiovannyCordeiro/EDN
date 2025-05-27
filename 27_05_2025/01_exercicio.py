def tip_calc(total_account: float, percantage: float) -> float:
  return (total_account * (1 + percantage / 100)) - total_account

print(tip_calc(300.0, 10.0))