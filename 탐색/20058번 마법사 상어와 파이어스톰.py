import sys
import copy
sys.setrecursionlimit(10**5)
def change(iw,w):
  copygraph = copy.deepcopy(graph)
  for k in range(0,iw,w):
    for o in range(0,iw,w):
      for i in range(w):
        for j in range(w):
          graph[k+j][o+w-i-1] = copygraph[k+i][o+j]

def melt(d,iw):
  copygraph = copy.deepcopy(graph)
  for i in range(iw):
    for j in range(iw):
      cnt = 0
      for k in d:
        if (0<=i+k[0]<iw) and (0<= j+k[1]<iw):
          if copygraph[i+k[0]][j+k[1]]:
            cnt+=1
      if cnt < 3 and graph[i][j]>0:
        graph[i][j]-=1

def dfs(x,y,d,iw,graph):
  result = 1
  for i in d:
    cdx = x + i[0]
    cdy = y + i[1]
    if (0<= cdx < iw) and (0<= cdy < iw) and (graph[cdx][cdy]>0):
      graph[cdx][cdy] = 0
      result += dfs(cdx,cdy,d,iw,graph)
  return result

if __name__ == '__main__':
  n , m = map(int,sys.stdin.readline().split())
  graph = [list(map(int,sys.stdin.readline().split())) for _ in range(2**n)]
  iw = 2**n
  d = [[1,0],[0,1],[-1,0],[0,-1]]
  skill = list(map(int,sys.stdin.readline().split()))
  sumresult = 0
  ans = 0

for i in skill:
  change(iw,2**i)
  melt(d,iw)

for j in range(iw):
  sumresult += sum(graph[j])
print(sumresult)

for x in range(iw):
  for y in range(iw):
    result = 1
    if graph[x][y] > 0:
      graph[x][y] = 0
      ans = max(ans,dfs(x,y,d,iw,graph))
print(ans)