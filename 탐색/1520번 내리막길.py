import sys
sys.setrecursionlimit(10**6)
m , n = map(int,sys.stdin.readline().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
visit = [[-1]*n for _ in range(m)]
dx = [0,-1,0,1]
dy = [1,0,-1,0]
def dfs(x,y):
  if x == (m-1) and y ==(n-1):
    return 1
  if visit[x][y] !=-1:
    return visit[x][y]
  visit[x][y]=0
  for i in range(4):
    cdx = x + dx[i]
    cdy = y + dy[i]
    if cdx<0 or cdx >= m or cdy <0 or cdy>=n or ground[x][y]<=ground[cdx][cdy]:
      continue
    visit[x][y]+=dfs(cdx,cdy)

  return visit[x][y]

dfs(0,0)
print(visit[0][0])
