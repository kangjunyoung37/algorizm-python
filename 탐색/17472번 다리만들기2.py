import sys
n,m = map(int,sys.stdin.readline().split())
island = [list(map(int,sys.stdin.readline().split()))for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
visit = [[False]*m for _ in range(n)]
def dfs(x,y,num):
  visit[x][y] = True
  island[x][y] = num
  position.append([x,y])#좌표 구하기
  for i in range(4):
    cdx = dx[i] + x
    cdy = dy[i] + y
    if cdx < 0 or cdy < 0 or cdx >= n or cdy >= m:
      continue
    if visit[cdx][cdy] == False and island[cdx][cdy] == 1:
      dfs(cdx,cdy,num)
num = 1
position = []
for i in range(n):
  for j in range(m):
    if visit[i][j] == False and island[i][j] == 1:
      dfs(i,j,num)
      num +=1
parent = [i for i in range(num)]
distance = []

def distancecheck(x,y):#가로 세로로 탐색
  cnt = 0
  for i in range(x+1,n):#세로 탐색  
    if island[i][y] == 0:#0개수를 세서 거리를 계산
      cnt +=1
    if island[i][y] == island[x][y]:
      break
    if island[i][y] != 0 and island[i][y] != island[x][y]:#0이 아니고 자기 자신의 숫자가 아니라면
      if cnt <= 1:
        break      
      distance.append((island[x][y],island[i][y],cnt))
      break
      
  cnt2 = 0
  for i in range(y+1,m): #가로 탐색
    if island[x][i] == 0:
      cnt2 +=1
    if island[x][i] == island[x][y]:
      break
    if island[x][i]!=0 and island[x][i] != island[x][y]: 
      if cnt2 <= 1:
        break        
      distance.append((island[x][y],island[x][i],cnt2))
      break 

for i in position:
  distancecheck(i[0],i[1])
distance = sorted(distance , key= lambda x : x[2])

def find_parent(parent,x):
  if parent[x] != x:
    parent[x] = find_parent(parent,parent[x])
  return parent[x]

def union(parent,a,b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)
  if a<b:
    parent[b] = a
  else:
    parent[a] = b

visit2 = [[False]*num for _ in range(num)]
result = 0
for start,end,cost in distance:
  if visit2[start][end] == False:
    visit2[start][end] = True
    if find_parent(parent,start) != find_parent(parent,end):
      union(parent,start,end)
      result += cost
ck = len(set(map(lambda x : find_parent(parent,x),parent)))

if ck == 2:
  print(result)
else:
  print(-1)

