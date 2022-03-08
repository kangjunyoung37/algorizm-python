import sys
n,m = map(int,sys.stdin.readline().split())
travel = 0
if n == 1:
  travel = 1
elif n == 2:
  travel = min(4,(m-1)//2+1)
elif m < 7:
  travel = min(4,m)
else:
  travel = ((m-5)+2)+1
print(travel)