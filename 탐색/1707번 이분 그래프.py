import sys
from collections import deque
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
def bfs(x):
  visit[x] = 1
  q = deque()
  q.append(x)
  while q:
    v = q.popleft()
    for i in graph[v]:
      if visit[i] == 0:
        visit[i] = -visit[v]
        q.append(i)
      else:
        if visit[i] == visit[v]:
          return False
  return True
    
for _ in range(n):
  a,b = map(int,sys.stdin.readline().split())
  number = [0] * (a+1)
  graph = [[] for _ in range(a+1)]
  visit = [0] * (a+1)
  isTrue = True
  for _ in range(b):
    num1,num2 = map(int, sys.stdin.readline().split())
    graph[num1].append(num2)
    graph[num2].append(num1)
  for i in range(1,a+1):
    if visit[i] == 0:
      if bfs(i) == False:
        isTrue = False
        break
  print("YES" if isTrue else "NO")