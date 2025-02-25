def solve(nums):
  nums.sort()
  for i, elem in enumerate(nums):
    if i != elem:
      return i
  return len(nums)
