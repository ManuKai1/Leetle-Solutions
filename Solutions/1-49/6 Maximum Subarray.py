def solve(nums):
  result = nums[0]
  kadane = nums[0]
  for i in range(1, len(nums)):
    kadane = max(kadane + nums[i], nums[i])
    result = max(kadane, result)
  return result
