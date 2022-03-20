import sys
sys.setrecursionlimit(10**6)
a , b = map(int,sys.stdin.readline().split())
node = [[0]*(a+1)for _ in range(a+1)]
visit = [False]*(a+1)
count = 0
for _ in range(b):
  c , d = map(int,sys.stdin.readline().split())
  node[c][d] = 1
  node[d][c] = 1
def dfs(start,visit,node):
  visit[start] = True
  for i in range(1, a+1):
    if visit[i] == False and node[start][i]==1:
      dfs(i,visit,node)
      
for i in range(1,a+1):
  if visit[i]==False:
    dfs(i,visit,node)
    count +=1
print(count)
  