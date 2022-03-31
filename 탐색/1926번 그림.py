import sys
sys.setrecursionlimit(1000000)
m , n = map(int,sys.stdin.readline().split())
picture  = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
result = []
def dfs(x,y):
  global cnt
  if x < 0 or x >= m or y < 0 or y >= n:
    return False
  if picture[x][y] == 1:
    picture[x][y] = 0
    cnt +=1
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    return True
  return False
cnt = 0
for i in range(m):
  for j in range(n
                ):
    if picture[i][j] == 1:
      dfs(i,j)
      result.append(cnt)
      cnt = 0
print(len(result))
if len(result) == 0:
  print(0)
else:
  print(max(result))

  

  
