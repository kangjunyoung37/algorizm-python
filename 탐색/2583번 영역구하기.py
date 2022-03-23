import sys
sys.setrecursionlimit(10**6)
n,m,k = map(int,sys.stdin.readline().split())
square= [[0]*m for _ in range(n)]
visit= [[False]*m for _ in range(n)]
for _ in range(k):
  a,b,c,d = map(int, sys.stdin.readline().split())
  for i in range(b,d):
    for j in range(a,c):
      square[i][j]=1
dx = [0,1,0,-1]
dy = [-1,0,1,0]
def dfs(x,y):
  global c
  if x< 0 or x>=n or y<0 or y>=m:
    return
  if square[x][y] ==0 and visit[x][y] ==False:
    visit[x][y]=True
    c+=1
    for i in range(4):
      dfs(x+dx[i],y+dy[i])
c=0
result = []
for i in range(n):
  for j in range(m):
    if square[i][j]==0 and visit[i][j]==False:
      dfs(i,j)
      result.append(c)
      c=0
print(len(result))
result.sort()
for i in result:
  print(i,end=" ")