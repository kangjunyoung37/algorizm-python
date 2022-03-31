import sys
sys.setrecursionlimit(10**9)
m , n = map(int,sys.stdin.readline().split())
cheeze = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
dx = [1,0,-1,0]
dy = [0,-1,0,1]
result = 0
def dfs(x,y):
  visit[x][y] = True
  for i in range(4):
    cdx = dx[i]+x
    cdy = dy[i]+y
    if cdx < 0 or cdx >=m or cdy < 0 or cdy >= n:
      continue
    if cheeze[cdx][cdy] == 0 and visit[cdx][cdy] == False:
      dfs(cdx,cdy)
        
def check(x,y):
  cnt = 0
  for i in range(4):
    cdx = dx[i]+x
    cdy = dy[i]+y 
    if cheeze[cdx][cdy] == 0 and visit[cdx][cdy] == True:
      cnt+=1
  if cnt >= 2:
    cheeze[x][y] = 0
k = 1
while k > 0:
  k = 0
  visit = [[False]*n for _ in range(m)]
  dfs(0,0)
  result +=1
  for i in range(m):
    for j in range(n):
      if cheeze[i][j] == 1:
        check(i,j)
        k+=1
print(result-1)