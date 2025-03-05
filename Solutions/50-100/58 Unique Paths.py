def solve(obstacleGrid):
  n = len(obstacleGrid[0])
  m = len(obstacleGrid)
  dp = [[0 for col in range(n)] for row in range(m)]
  blocked = False
  for i in range(m - 1, -1, -1):
    if obstacleGrid[i][n-1] == 1:
      blocked = True
    if blocked:
      dp[i][n - 1] = 0
    else:
      dp[i][n - 1] = 1
  blocked = False
  for j in range(n - 1, -1, -1):
    if obstacleGrid[m - 1][j] == 1:
      blocked = True
    if blocked:
      dp[m - 1][j] = 0
    else:
      dp[m - 1][j] = 1
  i = m - 2
  j = n - 2
  while i >= 0:
    j = n - 2
    while j >= 0:
      if obstacleGrid[i][j] == 1:
        dp[i][j] = 0
      else:
        dp[i][j] = dp[i + 1][j] + dp[i][j+1]
      j -= 1
    i -= 1
  return dp[0][0]
