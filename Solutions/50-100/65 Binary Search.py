def solve(nums, target):
  left, right = 0, len(nums) - 1
  while left <= right:
    middle = (left + right) // 2
    if nums[middle] == target:
      return middle
    elif nums[middle] > target:
      right = middle - 1
    else:
      left = middle + 1
  return -1

# Without implementing it ourselves:  
# import bisect
# def solve(nums, target):
#     i = bisect.bisect_left(nums,target)
#     if i != len(nums) and nums[i] == target:
#         return i
#     else:
#         return -1
