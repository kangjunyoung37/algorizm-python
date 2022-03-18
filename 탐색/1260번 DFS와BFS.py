import sys
from collections import deque
m,n,a  = map(int,sys.stdin.readline().split())

graph = [[]*(m+1)for _ in range(m+1)]
visited = [False]*(m+1)

for i in range(n):
  a , b  = map(int,sys.stdin.readline().split())
  
  graph[a].append(b)
  graph[b].append(a)

def dfs(graph,v,visited):
  visited[v] = True
  print(v,end=" ")
  for i in graph[v]:
    if not visited[i]:
      visited[i] = True
      dfs(graph,i,visited)
  visited = [False]*(m+1)

def bfs(graph,start,visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v,end=" ")
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
        bfs(graph,start,visited)
dfs(graph, a, visited)
print("")
bfs(graph, a, visited)



  
  