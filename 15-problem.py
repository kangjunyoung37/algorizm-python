import heapq
n = int(input())
number = [int(input()) for _ in range(n)]
result = 0
heapq.heapify(number)
while len(number)!=1:
  a = heapq.heappop(number)
  b = heapq.heappop(number)
  sum = a+b
  result+=sum
  heapq.heappush(number,sum)

print(result)