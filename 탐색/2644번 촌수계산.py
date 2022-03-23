import sys
n = int(sys.stdin.readline())
x , target = map(int , sys.stdin.readline().split())
people = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visit = [False]*(n+1)
for i in range(people):
  a , b = map(int , sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)
result = []
def dfs(x,c):
  c+=1
  visit[x] = True
  if x == target:
    result.append(c)
  for i in graph[x]:
    if visit[i] == False:
      dfs(i,c)

dfs(x,0)
if len(result)==0:
  print(-1)
else:
  print(result[0]-1)
  

