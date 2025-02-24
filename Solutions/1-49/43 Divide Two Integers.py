def solve(dividend, divisor):
  result = 0
  negative = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
  dividend = abs(dividend)
  divisor = abs(divisor)
  currentDivisor = divisor
  while currentDivisor <= dividend:
    result += 1
    currentDivisor += divisor
  if negative:
    return result - result - result
  return result
