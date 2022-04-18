import sys

def distance(a,b):
  return (a[0]-b[0])**2 + (a[1]-b[1])**2

def dfs(x):
  for i in range(n):
    if distance(location[x],location[i]) > (location[x][2]+location[i][2])**2 or i == x or visit[i] == True:#두 원이 인접해있는지 구하는 공식
      continue
    visit[i] = True
    dfs(i)

t = int(sys.stdin.readline())
for _ in range(t):
  n = int(sys.stdin.readline())
  result = 0
  location = []
  visit = [False] * n
  for _ in range(n):
    location.append(list(map(int,sys.stdin.readline().split())))
  for k in range(n):
    if visit[k] == False:
      dfs(k)
      result +=1
  print(result)