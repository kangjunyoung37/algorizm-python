import sys
a = int(sys.stdin.readline())
sys.setrecursionlimit(10**6)
result = []
for _ in range(a):
  m,n,k = map(int,sys.stdin.readline().split())
  kimchi = [[0]*m for _ in range(n)]
  visit = [[False]*m for _ in range(n)]
  count =0
  def dfs(x,y):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    if x<0 or x>=n or y>=m or y<0:
      return False
    if visit[x][y]==False and kimchi[x][y]==1:
      visit[x][y] = True
      for i in range(4):
        cdx = x+dx[i]
        cdy = y+dy[i]
        dfs(cdx,cdy)
      return True
    return False
  for i in range(k):
    c,d = map(int , sys.stdin.readline().split())
    kimchi[d][c] = 1
  for i in range(n):
    for j in range(m):
      if dfs(i,j)==True:
        count+=1
  result.append(count)
for i in result:
  print(i)
  