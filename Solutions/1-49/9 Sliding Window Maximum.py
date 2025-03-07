def solve(nums, k):
  left = 0
  l = []
  if len(nums) <= k:
    l.append(max(nums))
  else:
    while left + k - 1 < len(nums):
      currentList = []
      for j in range(k):
        currentList.append(nums[left + j])
      l.append(max(currentList))
      left += 1
  return l
