import sys
from collections import deque
m,n = map(int , sys.stdin.readline().split())
graph = [[] for _ in range(m+1)]
result = []
for _ in range(n):
  a,b = map(int,sys.stdin.readline().split())
  graph[b].append(a)
def bfs(x):
  visit = [False] * (m+1)
  visit[x] = True
  q = deque()
  q.append(x)
  cnt = 1
  while q:
    v = q.popleft()
    for i in graph[v]:
      if visit[i] == False:
        visit[i] = True
        q.append(i)
        cnt+=1
  return cnt
max_bfs = 0
for i in range(1,m+1):
  temp = bfs(i)
  if max_bfs == temp:
    result.append(i)
  if max_bfs < temp:
    result = []
    result.append(i)
    max_bfs = temp
print(*result)
    
      
    
