def solve(n):
  list = []
  for i in range(1, n + 1):
    if i % 15 == 0:
      list.append("FizzBuzz")
    elif i % 3 == 0:
      list.append("Fizz")
    elif i % 5 == 0:
      list.append("Buzz")
    else:
      list.append(i)
  return list
