import sys
n,m = map(int,sys.stdin.readline().split())
field = [list(map(str,sys.stdin.readline().rstrip())) for _ in range(n)]
visit = [[False]*m for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
result = [0,0]
def dfs(x,y):
  global sheep
  global fox
  if field[x][y] == 'o':
    sheep += 1
  if field[x][y] == 'v':
    fox += 1
  visit[x][y] = True
  for i in range(4):
    cdx = dx[i] + x
    cdy = dy[i] + y
    if cdx < 0 or cdy < 0 or cdx >= n or cdy >= m:
      continue
    if (field[cdx][cdy] == '.' or field[cdx][cdy] == 'o' or field[cdx][cdy] == 'v') and visit[cdx][cdy] == False:
      dfs(cdx,cdy)
      
for i in range(n):
  for j in range(m):
    if (field[i][j] == '.' or field[i][j] == 'o' or field[i][j] == 'v') and visit[i][j] == False:
      sheep = 0
      fox = 0
      dfs(i,j)
      if sheep > fox:
        result[0]+=sheep
      else:
        result[1]+=fox
print(*result)