import sys
n = int(sys.stdin.readline())
grade = []
sum = 0
for _ in range(n):
  grade.append(int(sys.stdin.readline()))
grade.sort()
for i in range(n):
  sum+= abs(grade[i]-(i+1))
print(sum)