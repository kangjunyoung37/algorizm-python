import sys
n = int(sys.stdin.readline())
money = []
moneychage = [25,10,5,1]
for _ in range(n):
  m = int(sys.stdin.readline())
  money.append(m) 
for i in range(n):
  for j in moneychage:
    print(money[i]//j, end=" ")
    money[i] = money[i]%j
  print("")
  