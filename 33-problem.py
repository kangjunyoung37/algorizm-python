import sys
gate = int(sys.stdin.readline())
plane = int(sys.stdin.readline())
doking = []
g = [x for x in range(gate+1)]

for _ in range(plane):
  a = int(sys.stdin.readline())
  doking.append(a)

def find_parent(x):
  if x == g[x]:
    return x
  y = find_parent(g[x])
  g[x] = y
  return g[x]
def union(x,y):
  x = find_parent(x)
  y = find_parent(y)
  g[x]=y
count = 0
for i in doking:
  pa = find_parent(i)
  if pa == 0:
    break
  else:
    union(pa,pa-1)
    count+=1
print(count)
  