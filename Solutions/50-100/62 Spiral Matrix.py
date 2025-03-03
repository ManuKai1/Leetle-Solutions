def solve(matrix):
  if len(matrix) == 0 or len(matrix[0]) == 0:
    return []
  n = len(matrix)
  m = len(matrix[0])
  visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
  solution = []
  i, j = 0, -1
  haveWeMoved = True
  while haveWeMoved:
      haveWeMoved = False
      # move right
      while j + 1 < m and not visited[i][j + 1]:
        solution.append(matrix[i][j + 1])
        visited[i][j + 1] = True
        haveWeMoved = True
        j += 1
      # move down
      while i + 1 < n and not visited[i + 1][j]:
        solution.append(matrix[i + 1][j])
        visited[i + 1][j] = True
        haveWeMoved = True
        i += 1
      # move left
      while j >= 1 and not visited[i][j - 1]:
        solution.append(matrix[i][j - 1])
        visited[i][j - 1] = True
        haveWeMoved = True
        j -= 1
      # move up
      while i >= 1 and not visited[i - 1][j]:
        solution.append(matrix[i - 1][j])
        visited[i - 1][j] = True
        haveWeMoved = True
        i -= 1
  return solution
