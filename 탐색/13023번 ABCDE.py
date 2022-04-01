import sys
from collections import deque
m , n = map(int,sys.stdin.readline().split())
graph = [[]for _ in range(m)]
visit = [False]*m
for _ in range(n):
  a , b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)
result = 0
def dfs(x,j):
  global result
  visit[x] = True
  if j == 4:
    result = 1
    return
  for i in graph[x]:
    if visit[i] == False:

      visit[i] == True
      dfs(i,j+1)     
      visit[i] == False
  visit[x] = False
for i in range(m):
  dfs(i,0)
  if result == 1:
    break
print(result)
  

  