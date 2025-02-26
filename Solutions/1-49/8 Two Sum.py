''' two pointers -> O(nlogn)
def solve(nums, target):
  sl = sorted(enumerate(nums), key=lambda x: x[1])
  left, right = 0, len(nums) - 1
  sum = 0
  result = []
  while left < right:
    if sl[left][1] + sl[right][1] == target:
      return sorted([sl[left][0], sl[right][0]])
    elif sl[left][1] + sl[right][1] < target:
      left += 1
    else:
      right -= 1
  return []
'''

# map -> O(n)
def solve(nums, target):
  map = {}
  for i in range(len(nums)):
    if target - nums[i] in map:
      return [map[target-nums[i]], i]
    else:
      map[nums[i]] = i
  return []
