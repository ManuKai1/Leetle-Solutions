def solve(strs):
  if not strs:
      return ""
  lcp = strs[0]
  for i in range(1, len(strs)):
      for j in range(len(lcp)):
          if j >= len(strs[i]):
              lcp = strs[i]
          elif lcp[j] != strs[i][j]:
              lcp = strs[i][:j]
              break
  return lcp
