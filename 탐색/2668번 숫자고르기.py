import sys
n = int(sys.stdin.readline())
num = [0]*(n+1)
result = []

for i in range(n):
  a = int(sys.stdin.readline())
  num[i+1] = a
  
def dfs(x,i):
  visit[x] = True
  if num[x] == i:
    result.append(i)
    return True
  if visit[num[x]]==False:
    visit[num[x]] = True
    dfs(num[x],i)
    visit[num[x]] = False
    
for i in range(1,n+1):
  visit = [False]*(n+1)
  dfs(i,i)
print(len(result))
for i in result:
  print(i)


  
  
    

