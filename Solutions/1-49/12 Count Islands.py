def bfs(graph, first, visited):
  from collections import deque
  q = deque()
  visited[first] = True
  q.append(first)
  while q:
    current = q.popleft()
    for other in graph[current]:
      if not visited[other]:
        visited[other] = True
        q.append(other)
    

def connectedComponents(grid, graph):
  count = 0
  current = 0
  v = len(graph)
  visited = [False] * v
  while current < v:
    if not visited[current] and grid[current // len(grid)][current % len(grid[0])] == 1:
      count += 1
      bfs(graph, current, visited)
    current += 1
  return count

def solve(grid):
  graph = [[] for _ in range(len(grid) * len(grid[0]))]
  current = 0
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j] == 1:
        if j + 1 < len(grid[i]):
          if grid[i][j+1] == 1:
            graph[current].append(current + 1)
            graph[current + 1].append(current)
        if i + 1 < len(grid):
          if grid[i+1][j] == 1:
            graph[current].append(current + len(grid[i]))
            graph[current + len(grid[i])].append(current)
      current += 1
  print(graph)
  return connectedComponents(grid, graph)
