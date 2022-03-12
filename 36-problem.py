import sys
n = int(sys.stdin.readline())
s = list(map(str,sys.stdin.readline()))
cup = n-(int(s.count('L')/2))+1
if cup>n:
  print(n)
else:
  print(cup)