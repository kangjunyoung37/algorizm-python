n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
sum = 0
a.sort()
for i in range(n):
  c = b.pop(b.index(max(b)))
  sum+=a[i]*c
print(sum) 
