import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
Tree = [[] for _ in range(n+1)]
parent = [0]*(n+1)
for _ in range(n-1):
  a,b = map(int,sys.stdin.readline().split())
  Tree[a].append(b)
  Tree[b].append(a)
def dfs(start,tree,parent):
  for i in tree[start]:
    if parent[i] == 0:
      parent[i]=start
      dfs(i,tree,parent)
dfs(1,Tree,parent)

for i in range(2,n+1):
  print(parent[i])
