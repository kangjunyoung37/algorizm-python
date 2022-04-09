import sys
sys.setrecursionlimit(10**6)
n,tree,q = map(int,sys.stdin.readline().split())
graph = [[]for _ in range(n+1)]
visit = [False] * (n+1)
cur_children = [0]*(n+1)
result = []
for _ in range(n-1):
  a,b = map(int,sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(x):
  visit[x] = True
  cur_children[x] = 1
  for i in graph[x]:
    if visit[i] == False:
      cur_children[x]+=dfs(i)
  return cur_children[x]

dfs(tree)

for _ in range(q):
  num = int(sys.stdin.readline())
  result.append(cur_children[num])
for i in result:
  print(i)
