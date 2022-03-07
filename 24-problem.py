import sys
n = int(sys.stdin.readline())
weight = list(map(int, sys.stdin.readline().split()))
weight.sort()
sum = 1
for i in weight:
  if i > sum:
    break
  sum+=i
print(sum)
