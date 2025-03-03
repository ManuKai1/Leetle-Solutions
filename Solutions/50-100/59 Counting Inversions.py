def solve(nums):
  inv = 0
  for i in range(len(nums)):
    for j in range(i, len(nums)):
      if nums[i] > nums[j]:
        inv += 1
  return inv
