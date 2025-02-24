def biggestPalindrome(s, i, j):
  while i >= 0 and j < len(s):
    if s[i] != s[j]:
      return s[i + 1:j]
    i -= 1
    j += 1
  return s[i + 1: j]

def solve(s):
  best = ""
  for i in range(len(s)):
    # s[i] is the center
    distanceToBorder = min(i, len(s) - i + 1)
    if 2*distanceToBorder < len(best):
      return best
    sOdd = biggestPalindrome(s, i - 1, i + 1)
    if len(sOdd) > len(best):
      best = sOdd
    sEven = biggestPalindrome(s, i, i + 1)
    if len(sEven) > len(best):
      best = sEven
  return best