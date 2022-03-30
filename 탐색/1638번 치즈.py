import sys
sys.setrecursionlimit(10**6)
m,n = map(int,sys.stdin.readline().split())
cheeze = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]
visit = [[False]*n for _ in range(m)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt = 1
result = 0
result2 = 0
def dfs(x,y):
  if x < 0 or x >= m or y <0 or y >= n:
    return
  visit[x][y] = True 
  for i in range(4):
    cdx = x+dx[i]
    cdy = y+dy[i]
    if cdx < 0 or cdx >= m or cdy < 0 or cdy >= n:
      continue
    if visit[cdx][cdy] == False and cheeze[cdx][cdy] == 0:
      dfs(cdx,cdy)
    elif visit[cdx][cdy] == False and cheeze[cdx][cdy] == 1:
      visit[cdx][cdy] = True
      cheeze[cdx][cdy] = 0
  return 
  
def dfs1(x,y):
  global cnt
  cnt+=1
  if x < 0 or x >= m or y <0 or y >= n:
    return
  visit[x][y] = True
  for i in range(4):
    cdx = x+dx[i]
    cdy = y+dy[i]
    if visit[cdx][cdy] == False and cheeze[cdx][cdy] == 1:
      visit[cdx][cdy] == True
      dfs1(cdx,cdy)

while True:

  cnt = 0
  for i in range(m):
    for j in range(n):
      if cheeze[i][j] == 1 and visit[i][j]==False:
        dfs1(i,j)
  if cnt == 0:
    break
  result2 = cnt
  
  visit = [[False]*n for _ in range(m)]
  dfs(0,0)
  result +=1
 

print(result)
print(result2)
  
  


  