import heapq
import sys
n= int(sys.stdin.readline())
study = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
study.sort()
room =[]
heapq.heappush(room,study[0][1])
for i in range(1,n):
  if study[i][0] < room[0]:
    heapq.heappush(room,study[i][1])
  else:
    heapq.heappop(room)
    heapq.heappush(room,study[i][1])
print(len(room))    

    