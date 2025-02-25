def solve(nums):
  dict = {}
  for elem in nums:
    if elem in dict:
      dict[elem] += 1
    else:
      dict[elem] = 1
  for elem in dict.items():
    if elem[1] == 1:
      return elem[0]
  return None
