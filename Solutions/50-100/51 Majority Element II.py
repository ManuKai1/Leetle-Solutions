def solve(nums):
  countMap = dict()
  for elem in nums:
    if elem in countMap:
      countMap[elem] += 1
    else:
      countMap[elem] = 1
  resultList = []
  for elem in countMap.keys():
    if countMap[elem] > len(nums) / 3:
      resultList.append(elem)
  return resultList