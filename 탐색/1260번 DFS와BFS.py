import sys
from collections import deque
m,n,q  = map(int,sys.stdin.readline().split())

graph = [[0]*(m+1)for _ in range(m+1)]
visited = [False]*(m+1)

for i in range(n):
  a , b  = map(int,sys.stdin.readline().split())
  graph[a][b] = 1
  graph[b][a] = 1
  
def dfs(graph,v,visited):
  visited[v] = True
  print(v,end=" ")
  for i in range(1,m+1):
    if not visited[i] and graph[v][i] == 1:
      dfs(graph, i ,visited)
    
def bfs(graph,start,visited):
  queue = deque([start])
  visited[start] = False
  while queue:
    v = queue.popleft()
    print(v,end=" ")
    for i in range(1,m+1):
      if visited[i] and graph[v][i] == 1:
        queue.append(i)
        visited[i] = False

dfs(graph, q, visited)
print("")
bfs(graph, q, visited)



  
  