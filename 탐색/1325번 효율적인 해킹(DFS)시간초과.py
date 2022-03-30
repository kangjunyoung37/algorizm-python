import sys
sys.setrecursionlimit(10**9)
m,n = map(int , sys.stdin.readline().split())
graph = [[] for _ in range(m+1)]
result = []
max_dfs = 0
for _ in range(n):
  a,b = map(int,sys.stdin.readline().split())
  graph[b].append(a)
cnt = 0
def dfs(x):
  global cnt
  visit[x] = True
  for i in graph[x]:
    if visit[i] == False:
      cnt +=1
      dfs(i)

for i in range(1,m+1):
  visit = [False]*(m+1)
  dfs(i)
  temp  = cnt
  cnt = 0
  if max_dfs == temp:
    result.append(i)
  if max_dfs < temp:
    result = []
    result.append(i)
    max_dfs = temp
print(*result)

    
