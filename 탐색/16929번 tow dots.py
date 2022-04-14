import sys
n, m= map(int,sys.stdin.readline().split())

graph = [list(map(str,sys.stdin.readline().rstrip())) for _ in range(n)]
visit = [[False]*m for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
ans = False

def dfs(x,y,cnt,start,end):
  global ans
  if ans == True:
    return
  for i in range(4):
    cdx = x + dx[i]
    cdy = y + dy[i]
    if cdx < 0 or cdy < 0 or cdx >= n or cdy >= m:
      continue 
    if cnt >=4 and cdx == start and cdy == end:
      ans = True
    if graph[cdx][cdy] == graph[x][y] and visit[cdx][cdy] == False:
      visit[cdx][cdy] = True
      dfs(cdx,cdy,cnt+1,start,end)
      visit[cdx][cdy] = False

for i in range(n):
  for j in range(m):
    if visit[i][j] == False:
      visit[i][j] = True
      dfs(i,j,1,i,j)
      if ans == True:
        print("Yes")
        exit()
print("No")

