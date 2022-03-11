import sys
n, m = map(int,sys.stdin.readline().split())
number = list(map(str, sys.stdin.readline().rstrip()))
stack = []
a = m
for i in range(n):
  while m > 0 and stack:
    if stack[len(stack)-1]<number[i]:
      stack.pop()
      m-=1
    else:
      break
  stack.append(number[i])
for i in range(n-a):
  print(stack[i],end="")
    