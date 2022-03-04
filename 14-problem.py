n = int(input())
alpa = [0]*26
a = [list(map(lambda x: ord(x)-65 ,input().rstrip())) for _ in range(n)]

for i in range(n):
  j = 0
  for w in a[i][::-1]:
    alpa[w]+=(10**j)
    j+=1
alpa.sort(reverse=True)
sum,t = 0,9
for i in range(26):
  if alpa[i] == 0:
    break
  sum += (alpa[i]*t)
  t-=1
print(sum)  
  