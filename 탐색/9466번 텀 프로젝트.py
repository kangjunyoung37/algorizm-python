import sys
sys.setrecursionlimit(10**6)
def dfs(x):
  visit[x] = 1
  team.append(x)
  a = student[x]
  if visit[a] == 1:
    if a in team:
      global cnt
      cnt += len(team[team.index(a):])
  else:
    dfs(a)

n = int(sys.stdin.readline())
for _ in range(n):
  people = int(sys.stdin.readline())
  student =[0] + list(map(int,sys.stdin.readline().split()))
  visit = [0]*(people+1)
  cnt = 0
  for i in range(1,people+1):
    if visit[i] == 0:
      team = [] #team을 새로운 i가 들어올 때마다 초기화 시켜줘야함
      dfs(i)
  print(people-cnt)