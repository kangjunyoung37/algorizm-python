n , money = map(int, input().split()) 
coins=[]
total = 0
for _ in range(n):
  a = int(input()) 
  coins.append(a)
coins.sort(reverse=True) 
for i in coins:
  if money % i == 0:
    total+=int(money/i)
    break
  elif money//i == 0:
    continue
  else:
    total+=int(money//i)
    money = (money%i)
    
print(total)