n = input()
sum = 0
if '0' not in n:
  print(-1)
else:
  for i in n:
    sum+=int(i)
  if sum%3!=0:
    print(-1)
  else:
    n = sorted(n,reverse = True)
    c = "".join(n)
    print(c)