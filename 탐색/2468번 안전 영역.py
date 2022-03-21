import sys
sys.setrecursionlimit(10**6)
n= int(sys.stdin.readline())
ground = [] 
result = []
count = 0
Max = 0
visit = [[False]*n for _ in range(n)]
for _ in range(n):
  a= list(map(int, sys.stdin.readline().split()))
  if Max < max(a):
    Max = max(a)
  ground.append(a)
def dfs(x,y,start):
  if x<0 or x>=n or y<0 or y>=n:
    return
  dx = [0,1,0,-1]
  dy = [-1,0,1,0]
  if ground[x][y] > start and visit[x][y] == False:
    visit[x][y] = True
    for i in range(4):
      cdx = dx[i]+x
      cdy = dy[i]+y
      dfs(cdx,cdy,start)
for k in range(0,Max):
  for i in range(n):
    for j in range(n):
      if ground[i][j] > k and visit[i][j] == False:
        dfs(i,j,k) 
        count +=1
        
  visit = [[False]*n for _ in range(n)]
  result.append(count)
  count = 0
print(max(result))
print(result)

    
  
     
  

  
    
    
  
