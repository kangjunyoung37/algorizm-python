import sys
import heapq
lost , brand = map(int, sys.stdin.readline().split())
pakage = []
one = []
total = []
for _ in range(brand):
  a,b = map(int, sys.stdin.readline().split())
  heapq.heappush(pakage , a)
  heapq.heappush(one , b)
pakageprice = heapq.heappop(pakage)
one = heapq.heappop(one)
heapq.heappush(total, one*lost)
if lost%6!=0: 
  
  b = pakageprice*(lost//6)
  a = (lost%6)*one
  heapq.heappush(total,b+pakageprice)
  heapq.heappush(total,a+b)

else:
  heapq.heappush(total, pakageprice*(lost//6))
print(heapq.heappop(total))
  