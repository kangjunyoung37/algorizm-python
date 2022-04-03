import sys
n,m,k = map(int,sys.stdin.readline().split())
graph = [[0]*m for _ in range(n)]
visit = [[False]*m for _ in range(n)]
for _ in range(k):
  a,b = map(int,sys.stdin.readline().split())
  graph[a-1][b-1] = 1 
dx = [0,1,-1,0]
dy = [1,0,0,-1]
result = []
def dfs(x,y):
  global cnt
  visit[x][y] = True
  for i in range(4):
    cdx = dx[i]+x
    cdy = dy[i]+y
    if cdx < 0 or cdx >=n or cdy <0 or cdy >=m:
      continue
    if visit[cdx][cdy]==False and graph[cdx][cdy] == 1:
      visit[cdx][cdy] = True
      cnt +=1
      dfs(cdx,cdy)

for i in range(n):
  for j in range(m):
    if visit[i][j] == False and graph[i][j] == 1:
      cnt = 1
      dfs(i,j)
      result.append(cnt)
print(max(result))

