a = int(input())
group = []
for _ in range(a):
  n = int(input())
  a = list(map(int,input().split()))
  a.sort()
  Max = a[1]-a[0]
  for i in range(n-2):
    Max = max( Max ,a[i+2]-a[i])
  Max = max(Max, a[len(a)-1]-a[len(a)-2])
  group.append(Max)
for i in range(3):
  print(group[i])

    
     