money = int(input())
change = 1000-money
coins = [500,100,50,10,5,1]
sum = 0
for i in coins:
  if change//i == 0:
    continue
  else:
    sum+=change//i
    change%=i
   
print(sum)