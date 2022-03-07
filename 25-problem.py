import sys
a , tape = map(int ,sys.stdin.readline().split())
hole =list(map(int,sys.stdin.readline().split()))
hole.sort()
sum = hole[0]+(-0.5+tape)
total = 1
for i in range(1,a):
  if sum >= hole[i]+0.5:
    continue
  elif sum < hole[i]+0.5:
    sum = hole[i]+(-0.5+tape)
    total+=1
print(total)    
  

  