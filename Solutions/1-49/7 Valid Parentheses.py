def solve(s):
  stack = []
  for char in s:
    if char == ')':
      top = stack.pop()
      if top != '(':
        return False
    elif char == ']':
      top = stack.pop()
      if top != '[':
        return False
    elif char == '}':
      top = stack.pop()
      if top != '{':
        return False
    else:
      stack.append(char)
  return len(stack) == 0
