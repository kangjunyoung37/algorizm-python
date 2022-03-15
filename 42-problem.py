a = input()
b = list(map(str,input().rstrip()))

n = len(b)
while n>len(a):
  if b[n-1] == "A":
    b.pop(n-1)
    n-=1
  elif b[n-1] == "B":
    b.pop(n-1)
    b.reverse()
    n-=1
if "".join(b) == a:
  print(1)
else:
  print(0)