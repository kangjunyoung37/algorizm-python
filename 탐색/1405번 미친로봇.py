import sys
N,e,w,n,s = map(int,sys.stdin.readline().split())
percent = [e*0.01,w*0.01,s*0.01,n*0.01]
visit =[[False]*29 for _ in range(29)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
ans = 0
def dfs(x,y,total,result):
  global ans
  visit[x][y] = True
  for i in range(4):
    cdx = x+dx[i]
    cdy = y+dy[i]
    if visit[cdx][cdy] == False:
      if total >= N:
        ans += result * percent[i]
      else:
        dfs(cdx,cdy,total+1,result*percent[i])
  visit[x][y] = False
dfs(14,14,1,1)
print(ans)

        
      