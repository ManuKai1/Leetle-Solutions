def solve(nums):
  # also doable with a set
  dic = {}
  for num in nums:
    if num > 0:
      dic[num] = 1
  current = 1
  while current in dic:
      current += 1
  return current
