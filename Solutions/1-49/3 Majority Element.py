def solve(nums):
  counter = 0
  majority = None
  for elem in nums:
    if counter == 0:
      majority = elem
      counter = 1
    elif elem == majority:
      counter += 1
    else:
      counter = counter - 1
  return majority
