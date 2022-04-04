import sys
n,m = map(int,sys.stdin.readline().split())
g = []
for _ in range(n):
  a = list(map(str,sys.stdin.readline().rstrip()))
  g.append(a)
dy = [1,1,1]
dx = [-1,0,1]
visit = [[False]*m for _ in range(n)]
def dfs(x,y):
  global cnt
  visit[x][y] = True
  if y == m-1:
    cnt = True
    return
  for i in range(3):
    cdx = x+dx[i]
    cdy = y+dy[i]
    if cnt == True:
      return
    if cdx < 0 or cdx >= n or cdy<0 or cdy >=m:
      continue
    if visit[cdx][cdy] == False and g[cdx][cdy] == ".":
      dfs(cdx,cdy)
result = 0
for i in range(n):
  cnt = False
  dfs(i,0)
  if cnt == True:
    result +=1
print(result)
  
    

