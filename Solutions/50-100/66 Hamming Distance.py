def solve(x, y):
  xor = x ^ y
  return xor.bit_count()
