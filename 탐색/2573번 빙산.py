import sys
from collections import deque
n, m = map(int,sys.stdin.readline().split())
ground = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def melt(visit):

  for i in range(n):
    for j in range(m):
      cnt = 0
      if ground[i][j] != 0:
        visit[i][j] = 1
        for k in range(4):
          cdx = i+dx[k]
          cdy = j+dy[k]
          if 0 <= cdx <n and 0<= cdy < m and ground[cdx][cdy] ==0 and visit[cdx][cdy] == 0:            
            cnt+=1
        ground[i][j] = max(0,ground[i][j]-cnt)


def bfs(x,y):
  queue = deque([(x,y)])
  visit[x][y] = 0
  while queue:
    x,y = queue.popleft()
    for i in range(4):
      cdx = x + dx[i]
      cdy = y + dy[i]
      if 0 <=cdx < n and 0<=cdy <m and visit[cdx][cdy] == 1:
        visit[cdx][cdy] = 0
        queue.append((cdx,cdy))

      
year = 0
while True:
  count = 0
  visit = [[0]*m for _ in range(n)]
  melt(visit)
  year+=1
  
  for i in range(1,n-1):
    for j in range(1,m-1):
      if visit[i][j] == 1:
        count+=1  
        bfs(i,j)

  if count == 0:
    print(0)
    break
    
  if count >= 2:
    print(year-1)
    break