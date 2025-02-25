def solve(nums, k):
  copyNums = nums.copy()
  for i in range(len(nums)):
    nums[(i + k) % len(nums)] = copyNums[i]
  return nums
