import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
panda = []
for _ in range(n):
  panda.append(list(map(int , sys.stdin.readline().split())))
visit = [[0]*n for _ in range(n)]
dx = [0,1,-1,0]
dy = [-1,0,0,1]

def dfs(x,y,visit):
  if visit[x][y]:
    return visit[x][y]
  visit[x][y] = 1  
  for i in range(4):
    cdx = x + dx[i]
    cdy = y + dy[i]
    if 0 <= cdx <n and 0<=cdy <n and panda[x][y]<panda[cdx][cdy]:
      visit[x][y] = max(visit[x][y],dfs(cdx,cdy,visit)+1)
  return visit[x][y]
  
result = 0
for i in range(n):
  for j in range(n):
    result = max(result,dfs(i,j,visit))
print(result)