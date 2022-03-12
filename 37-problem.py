import sys
n , m = map(int, sys.stdin.readline().split())
number = list(map(int , sys.stdin.readline().split()))
number.sort()
sum = 0
for _ in range(m):
  a = number[0]+number[1]
  number[0]=number[1]=a
  number.sort()
for i in range(n):
  sum+=number[i]
print(sum)