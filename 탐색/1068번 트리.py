import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
node = list(map(int,sys.stdin.readline().split()))
de = int(sys.stdin.readline())
graph = [[] for _ in range(n)]
visit = [False] * n
cnt = 0
for i in range(n):
  if node[i] == -1:
    continue
  graph[node[i]].append(i)
def dfs(x):
  visit[x] = True
  for i in graph[x]:
    if i == "":
      break
    visit[i] = True
    dfs(i)
dfs(de)

for i in range(n):
  if visit[i]==False and graph[i] ==[]:
    cnt +=1
  elif len(graph[i])== 1 and visit[i] == False and visit[graph[i][0]] == True:
    cnt +=1
  elif visit.count(False) == 1 and node[i] == -1: 
    cnt+=1
    break
print(cnt)