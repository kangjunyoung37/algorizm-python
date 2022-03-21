import sys
sys.setrecursionlimit(10**6)
x=1
y=1
result = []
def dfs(c,d):
  
  if c < 0 or c>=x or d <0 or d>=y:
    return 
  
  dx = [0,1,0,-1,-1,-1,1,1]
  dy = [1,0,-1,0,-1,1,-1,1]
  if ground[c][d]==1 and visit[c][d] == False:
    visit[c][d] = True
    for i in range(8):
      cdx = dx[i]+c
      cdy = dy[i]+d
      dfs(cdx,cdy)
  
while x!=0 or y!=0:
  y, x = map(int, sys.stdin.readline().split())
  if x == 0 and y == 0:
    break
  visit =  [[False]*y for _ in range(x)]
  ground = []
  count = 0

  for _ in range(x):
    a = list(map(int,sys.stdin.readline().split()))
    ground.append(a)
  for i in range(x):
    for j in range(y):
      if visit[i][j] == False and ground[i][j]==1:
        dfs(i,j)
        count+=1
  result.append(count)
for i in result:
  print(i)
  

  
    
    
  
