def solve(a, b):
  i = len(a) - 1
  j = len(b) - 1
  result = ""
  carry = False
  while i >= 0 and j >= 0:
    if carry:
      if a[i] == '1' and b[j] == '1':
        carry = True
        result = "1" + result
      elif a[i] == '1' or b[j] == '1':
        carry = True
        result = "0" + result
      else:
        carry = False
        result = "1" + result
    else:
      if a[i] == '1' and b[j] == '1':
        carry = True
        result = "0" + result
      elif a[i] == '1' or b[j] == '1':
        carry = False
        result = "1" + result
      else:
        carry = False
        result = "0" + result
    i -= 1
    j -= 1
  while i >= 0:
    if carry:
      if a[i] == '1':
        result = "0" + result
      else:
        carry = False
        result = "1" + result
    else:
      result = a[i] + result
    i -= 1
  while j >= 0:
    if carry:
      if b[j] == '1':
        result = "0" + result
      else:
        carry = False
        result = "1" + result
    else:
      result = b[j] + result
    j -= 1
  if carry:
      result = "1" + result
  return result