n = int(input())
a = []
for _ in range(n):
  rope = int(input())
  a.append(rope)
a.sort(reverse = True)
b = []
for i in range(n):
  b.append(a[i]*(i+1))
print(max(b))  
  