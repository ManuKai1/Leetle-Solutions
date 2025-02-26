def isPalindrome(s):
  for i in range(len(s)//2):
    if s[i] != s[len(s) - 1 - i]:
      return False
  return True

def solve(s):
  for i in range(len(s)//2):
    if s[i] != s[len(s) - 1 - i]:
      s1 = s[:i] + s[i+1:]
      s2 = s[:len(s) - 1 - i] + s[len(s) - i:]
      return isPalindrome(s1) or isPalindrome(s2)
  return True
