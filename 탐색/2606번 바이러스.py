import sys
a = int(sys.stdin.readline())
visit = [False]*(a+1)
node = [[0]*(a+1) for _ in range(a+1)]
b = int(sys.stdin.readline())
for _ in range(b):
  c,d = map(int,sys.stdin.readline().split())
  node[c][d] = 1
  node[d][c] = 1
def dfs(node,start,visit):
  visit[start] = True
  global c
  for i in range(a+1):
    if visit[i]==False and node[start][i] == 1:
      c+=1
      dfs(node,i,visit)
c = 0
dfs(node,1,visit)
print(c)