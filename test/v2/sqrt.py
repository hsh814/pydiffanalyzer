def sqrt(x: float) -> float:
  x1: float
  x2: float
  x3: float = 1.0
  eps: float = 0.001
  errval: float = 0.0
  if (x <= 0.0):
    print("illegal operand")
    return errval
  else:
    if (x < 1):
      x1 = x
      x2 = 1
    else:
      x1 = eps
      x2 = x
    while ((x2 - x1) >= 2.0 * eps):
      x3 = (x1 + x2) / 2.0
      if (x3 * x3 - x) * (x1 * x1 - x) < 0:
        x2 = x3
      else:
        x1 = x3
    return x3