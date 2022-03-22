import sys
m,n = map(int,sys.stdin.readline().split())
alpa = [list(map(lambda a: ord(a)-65,sys.stdin.readline().rstrip())) for _ in range(m)]
visit = [False]*26
dx,dy = [0,1,0,-1],[1,0,-1,0]

def dfs(x,y,cnt):
  global result
  result = max(result,cnt)

  for i in range(4):
    nx, ny = x+dx[i], y+dy[i]
    if 0 <= nx < m and 0<=ny<n and visit[alpa[nx][ny]] == False:
      visit[alpa[nx][ny]] = True
      dfs(nx,ny,cnt+1)
      visit[alpa[nx][ny]] = False
result = 0
visit[alpa[0][0]] = True
dfs(0,0,1)
print(result)