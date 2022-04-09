import sys
m,n = map(int, sys.stdin.readline().split())
s = [list(map(str,sys.stdin.readline().rstrip())) for _ in range(n)]
visit = [[False]*m for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
result = [0,0]

def dfs1(x,y):
  visit[x][y] = True
  global cnt
  for i in range(4):
    cdx = dx[i]+x
    cdy = dy[i]+y
    if cdx < 0 or cdy <0 or cdx >= n or cdy >=m:
      continue
    if s[cdx][cdy] == "W" and visit[cdx][cdy] == False:
      dfs1(cdx,cdy) 
      cnt += 1
      
def dfs2(x,y):
  visit[x][y] = True
  global cnt2
  for i in range(4):
    cdx = dx[i]+x
    cdy = dy[i]+y
    if cdx < 0 or cdy <0 or cdx >= n or cdy >=m:
      continue
    if s[cdx][cdy] == "B" and visit[cdx][cdy] == False:
      dfs2(cdx,cdy) 
      cnt2 += 1
      
for i in range(n):
  for j in range(m):
    if visit[i][j] == False:
      if s[i][j] == "W":
        cnt = 1
        dfs1(i,j)
        result[0] += cnt**2
      if s[i][j] == "B":
        cnt2 = 1
        dfs2(i,j)
        result[1] += cnt2**2  
print(*result)