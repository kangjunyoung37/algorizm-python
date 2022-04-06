import sys
sys.setrecursionlimit(10**5)
n = int(sys.stdin.readline())
a = [[0]*2 for _ in range(n+1)]
row = [[]for _ in range(n+1)]
node2 = [0 for _ in range(n+1)]
for _ in range(n):
  node,right,left = map(int,sys.stdin.readline().split())
  a[node][0] = left
  a[node][1] = right
  node2[node] +=1
  if right != -1:
    node2[right] +=1
  if left != -1:
    node2[left] +=1
def visit(node,level):
  global num
  if a[node][0] != -1:
    visit(a[node][0],level+1)
  row[level].append(num)
  num+=1
  if a[node][1] != -1:
    visit(a[node][1], level+1)
root = 0
for i in range(1,n+1):
  if node2[i] == 1:
   root = i 
num = 1
visit(root,1)
result = 0
level = 0
for i in range(1,n+1):
  if row[i]:  
    if result < max(row[i])-min(row[i])+1:
      result = max(row[i])-min(row[i])+1
      level = i
print(level,end =" ")
print(result)
  