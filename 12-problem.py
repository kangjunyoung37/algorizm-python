n = int(input())
distance = list(map(int,input().split()))
price = list(map(int,input().split()))
totalprice = 0
start=price[0]
for i in range(len(distance)):
  if start > price[i]:
    start = price[i]
  totalprice+=start*distance[i]
print(totalprice)