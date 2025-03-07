def solve(s):
  newS = ""
  for c in s:
    if c.isalnum():
      newS = newS + c.lower()
  left = 0
  right = len(newS) - 1
  # Alternative to the following lines: return s == s[::-1]
  while left < right:
    if newS[left] != newS[right]:
      return False
    left += 1
    right -= 1
  return True
