import sys
n = int(sys.stdin.readline())
total = []
for _ in range(n):
  score = []
  case = int(sys.stdin.readline())
  for _ in range(case):
    a , b = map(int, sys.stdin.readline().split())
    score.append([a,b])
  score.sort()
 
  sum = 0
  start = score[0][1]
  for i in range(case):
    if start >= score[i][1]:
      sum+=1
      start = score[i][1]
  total.append(sum)
for i in range(n):
  print(total[i])