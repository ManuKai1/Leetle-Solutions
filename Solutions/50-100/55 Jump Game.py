def solve(nums):
  for i in range(len(nums) - 1):
    if nums[i] == 0:
      j = i - 1
      while j >= 0:
        if nums[j] > i - j:
          break
        j -= 1
      if j < 0:
        return False
  return True
