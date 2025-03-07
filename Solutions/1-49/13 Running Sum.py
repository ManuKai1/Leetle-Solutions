def solve(nums):
  sum = 0
  result = []
  for elem in nums:
    sum += elem
    result.append(sum)
  return result
