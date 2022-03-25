import sys
from collections import deque

n =int( sys.stdin.readline())
graph = [[]for _ in range(n+1)]

for _ in range(n-1):
  a,b,distance = map(int,sys.stdin.readline().split())
  graph[a].append((b,distance))
  graph[b].append((a,distance))
  
def bfs(x):
  q = deque()
  q.append((x,0))
  visit = [False]*(n+1)
  visit[x] = True
  
  result = [0,0]
  
  while q:
    now,cnt = q.popleft()

    for i in graph[now]:
      ne,value = i[0],i[1]

      if visit[ne]==False:
        visit[ne]=True

        q.append((ne,cnt+value))
        if result[1]< cnt+value:
          result[1] = cnt+value
          result[0] = ne
  return result

l = bfs(1)
ml = bfs(l[0])
print(ml[1])

        
      
    

