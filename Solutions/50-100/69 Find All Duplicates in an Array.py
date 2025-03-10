def solve(nums):
  count = [0 for i in range(len(nums) + 1)]
  result = []
  for elem in nums:
    count[elem] += 1
  for i, c in enumerate(count):
    if c == 2:
      result.append(i)
  return result
