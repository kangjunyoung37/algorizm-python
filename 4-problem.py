n = int(input())
time = []
for _ in range(n):
  a = list(map(int, input().split()))
  time.append(a)
time = sorted(time , key = lambda x:x[0])  
time = sorted(time , key = lambda x:x[1])
last = 0
total = 0
for i, j in time:
  if i >=last:
    total+=1
    last = j
print(total)