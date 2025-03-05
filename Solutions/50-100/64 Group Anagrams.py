def solve(strs):
  anagramMap = {}
  for s in strs:
    sort = "".join(sorted(s))
    if sort in anagramMap:
      anagramMap[sort].append(s)
    else:
      anagramMap[sort] = [s]
  return list(anagramMap.values())
