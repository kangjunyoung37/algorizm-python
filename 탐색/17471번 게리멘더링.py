import sys
from collections import deque
n = int(sys.stdin.readline())
distance  = list(map(int,sys.stdin.readline().split()))
g = [[]for _ in range(n+1)]
for i in range(1,n+1):
  a = list(map(int,sys.stdin.readline().split()))
  for j in range(a[0]):
    g[i].append(a[j+1])
result = 10000

def bfs(w):
  q = deque()
  q.append(w[0])
  check = [False]*(n+1)
  check[w[0]] = True
  c , ans = 1,0
  while q:
    v = q.popleft()
    ans += distance[v-1]
    for i in g[v]:
      if i in w and not check[i]:
        check[i] = True
        q.append(i)
        c +=1
  if c == len(w):
    return ans
  else: 
    return False

def dfs(cnt , x , end):
  global result
  visit[x] = True
  if cnt == end:
    q1,q2 = deque(),deque() 
    for i in range(1,n+1):
      if visit[i]:
        q1.append(i)
      else:
        q2.append(i)
    result1 = bfs(q1)
    if result1 == False:
      return
    result2 = bfs(q2)
    if result2 == False:
      return
    result = min(result,abs(result1-result2))
  for j in range(x,n+1):
    if visit[j]:
      continue
    visit[j] = True
    dfs(cnt+1,j,end)
    visit[j] = False
for i in range(1,n//2+1):
  visit = [True]+[False]*n
  dfs(0,0,i)
if result == 10000:
  print(-1)
else:
  print(result)
      
      
      