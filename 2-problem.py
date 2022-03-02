n = int(input())

time = list(map(int,input().split()))

time.sort()

sum = 0

for i in range(n+1):
  
  for j in range(i):
   
    sum += time[j]
      
print(sum)
