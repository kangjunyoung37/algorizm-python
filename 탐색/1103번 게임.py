import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n,m = map(int,input().split())
board = [list(map(str,input().rstrip())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
dp = [[0]*m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0
def move(x,y,cnt):
  global result
  result = max(result,cnt)
  for i in range(4):
    cdx = x + dx[i]*int(board[x][y])
    cdy = y + dy[i]*int(board[x][y])
    if 0 <= cdx < n and 0 <= cdy <m and board[cdx][cdy] != 'H' and cnt > dp[cdx][cdy]:
      if visit[cdx][cdy] == 1:
        print(-1)
        exit()
      else:
        dp[cdx][cdy] = cnt
        visit[cdx][cdy] = 1
        move(cdx,cdy,cnt+1)
        visit[cdx][cdy] = 0
move(0,0,1)
print(result)
