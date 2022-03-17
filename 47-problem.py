import sys
a = int(sys.stdin.readline())
N = []
for _ in range(a):
  day , score = map(int ,sys.stdin.readline().split())
  N.append([day,score])
N = sorted(N,key = lambda x:(-x[1]))
result = [0]*1001
for day,score in N:
  if result[day] == 0:
    result[day] = score
  else:
    while(day>0):
      if result[day]==0:
        result[day]=score
        break
      day-=1
print(sum(result))

  
