import sys
import heapq
dia , bag = map(int,sys.stdin.readline().split())

diaimpo = []
for _ in range(dia):
  w,p = map(int,sys.stdin.readline().split())
  heapq.heappush(diaimpo ,[w,p])
 
bagimpo = []
for _ in range(bag):
  bw = int(sys.stdin.readline())
  heapq.heappush(bagimpo, bw)

sum = 0
temp = []
for _ in range(bag):
  bagw = heapq.heappop(bagimpo)
  while diaimpo and bagw >= diaimpo[0][0]:
    [w,p] = heapq.heappop(diaimpo)
    heapq.heappush(temp , -p)
  if temp:
    sum -= heapq.heappop(temp)
  elif not diaimpo:
    break
print(sum)    
  