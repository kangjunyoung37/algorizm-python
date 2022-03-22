import sys
sys.setrecursionlimit(10**6)
n= int(sys.stdin.readline())
color = []
visit = [[False]*n for _ in range(n)]
for _ in range(n):
  a = list(map(str,sys.stdin.readline().rstrip()))
  color.append(a)
def dfs(x,y,c,color,visit):
  if x < 0 or x >= n or y < 0 or y >= n:
    return
  dx=[0,1,-1,0]
  dy= [1,0,0,-1]
  if color[x][y]==c and visit[x][y]== False:
    visit[x][y]=True
    for i in range(4):
      dfs(x+dx[i],y+dy[i],c,color,visit)
color2=[[0]*n for _ in range(n)]
visit2=[[False]*n for _ in range(n)]
for i in range(n):
  for j in range(n):
    if color[i][j]=='G'or color[i][j]== 'R':
      color2[i][j]= 'R'
    else:
      color2[i][j]='B'
count=0
count2= 0
for i in range(n):
  for j in range(n):
    if visit[i][j]==False:
      dfs(i,j,color[i][j],color,visit)
      count+=1
      
    if visit2[i][j]==False:
      dfs(i,j,color2[i][j],color2,visit2)
      count2+=1
print(count,count2)
