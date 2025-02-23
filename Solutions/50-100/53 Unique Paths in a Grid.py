def solve(m, n):
  dp = [[0 for col in range(n)] for row in range(m)]
  for i in range(m):
    dp[i][n - 1] = 1
  for j in range(n):
    dp[m - 1][j] = 1
  i = m - 2
  j = n - 2
  while i >= 0:
    j = n - 2
    while j >= 0:
      dp[i][j] = dp[i + 1][j] + dp[i][j+1]
      j -= 1
    i -= 1
  return dp[0][0]
