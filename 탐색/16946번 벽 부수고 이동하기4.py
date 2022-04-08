import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split(" "))
room = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
floor = [[0]*m for _ in range(n)]
visit = [[False]*m for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
group = 1
impo = {}
def bfs(x,y):
  q = deque()
  q.append((x,y))
  cnt = 1
  visit[x][y] = True
  while q:
    a ,b  = q.popleft()
    floor[a][b] = group
    for i in range(4):
      cdx = a + dx[i]
      cdy = b + dy[i]
      if cdx < 0 or cdy < 0 or cdx >= n or cdy >= m:
        continue
      if visit[cdx][cdy] == False and room[cdx][cdy] == 0:
        visit[cdx][cdy] = True
        q.append((cdx,cdy))
        cnt +=1
  return cnt
  
def calculate(x,y):
  calcu = set()
  for i in range(4):
    cdx = x+dx[i]
    cdy = y+dy[i]
    if cdx < 0 or cdy < 0 or cdx >= n or cdy >=m:
      continue
    if room[cdx][cdy] == 0:
      calcu.add(floor[cdx][cdy])
  cnt = 1
  for j in calcu:
    cnt += impo[j]
    cnt %= 10
  return cnt
  
for i in range(n):
  for j in range(m):
    if visit[i][j] == False and room[i][j] == 0:
      cnt = bfs(i,j)
      impo[group] = cnt
      group+=1
result = [[0]*m for _ in range(n)]
for i in range(n):
  for j in range(m):
    if room[i][j] == 1:
      cnt2 = calculate(i,j)
      result[i][j] = cnt2
    print(result[i][j],end = "")
  print("")

      
      
       
      
    



    
  