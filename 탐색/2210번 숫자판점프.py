import sys
g = [list(map(str,sys.stdin.readline().split())) for _ in range(5)]
dx = [0,1,-1,0]
dy = [-1,0,0,1]
ans = []
def dfs(x,y,result):
  if len(result) == 6:#result 길이가 6이 되면
    if result not in ans:#중복값 제거
      ans.append(result)
    return#중복값이 있을 경우에도 리턴을 해줌
  for i in range(4):
    cdx = dx[i] + x
    cdy = dy[i] + y
    if cdx < 0 or cdy < 0 or cdx >= 5 or cdy >= 5:
      continue
    else:
      dfs(cdx,cdy,result+g[cdx][cdy])
for i in range(5):
  for j in range(5):
    dfs(i,j,g[i][j])
print(len(ans))   