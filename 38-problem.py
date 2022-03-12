import sys
n  = int(sys.stdin.readline())
m = int(sys.stdin.readline())
house = list(map(int,sys.stdin.readline().split()))
house.sort()
dis = []
for i in range(n-1):
  dis.append(house[i+1]-house[i])

for _ in range(m-1):
  if len(dis) == 0:
    dis.append(0)
  else:
    dis.pop(dis.index(max(dis)))
print(sum(dis))

