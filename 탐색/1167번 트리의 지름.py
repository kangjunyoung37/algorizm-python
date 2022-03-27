import sys
from collections import deque
n = int(sys.stdin.readline())
graph = [[]for _ in range(n+1)]
for _ in range(n):
  a = list(map(int,sys.stdin.readline().split()))
  for i in range(1,len(a)-2,2):
    graph[a[0]].append(a[i:i+2])

def bfs(x):#너비 우선 탐색
  q = deque()
  q.append((x,0))
  visit = [False]*(n+1)
  visit[x] = True  
  result = [0,0]
  while q:
    v , cnt = q.popleft()
    for i in graph[v]:
      node = i[0]
      value =i[1]
     
      if visit[node] == False:
        visit[node] = True
        q.append((node,cnt+value))
        
        if result[1] < cnt+value:
          result[0] = node
          result[1] = cnt+value
  return result
l = bfs(1)
re = bfs(l[0])
print(re[1])
      
    
    