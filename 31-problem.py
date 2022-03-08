import sys
n,m = map(int, (sys.stdin.readline().split()))
house = [list(map(str,sys.stdin.readline().rstrip('\n'))) for _ in range(n)]
visited = [[False] *m for _ in range(n)]
dx = [-1,0,1]
dy = [1,1,1]
def dfs(x,y,visited):
  global flag
  visited[x][y] = True

  if y == m-1:
    flag = True
    return
  for i in range(3):
    nx = x + dx[i]
    ny = y + dy[i]
    if flag == True:
      return
    if nx < 0 or ny < 0 or nx >=n or ny >= m:
      continue
    if house[nx][ny] == "." and not visited[nx][ny]:
      dfs(nx,ny,visited)
count = 0
for i in range(n):
  flag = False
  dfs(i,0,visited)
  if flag == True:
    count+=1
print(count)    