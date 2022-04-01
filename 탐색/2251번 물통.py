import sys
from collections import deque
A,B,C = map(int,sys.stdin.readline().split())
visit = [[False]*(B+1) for _ in range(A+1)]
answer = []
def visited(a,b):
  if visit[a][b] == False:
    visit[a][b] = True
    q.append((a,b))
def bfs():
  while q:
    a,b = q.popleft()
    c = C - (a+b)
    if a == 0:
      answer.append(c)
    #6가지 경우
    #A->C
    if a > 0 and c < C:
      water = min(a,C-c)#옮길 수 있는 물의 양
      visited(a-water,b)
    #A->B
    if a > 0 and b < B:
      water = min(a,B-b)
      visited(a-water,b+water)
    #B->C
    if b > 0 and c < C:
      water = min(b,C-c)
      visited(a,b-water)
    #B->A
    if b > 0 and a < A:
      water = min(b, A-a)
      visited(a+water,b-water)
    #C->A
    if c > 0 and a < A:
      water = min(c,A-a)
      visited(a+water, b)
    #C->B
    if c > 0 and b < B:
      water = min(c,B-b)
      visited(a,b+water)
q = deque()
q.append((0,0))
visit[0][0] = True
bfs()
answer.sort()
for i in answer:
  print(i, end = " ")
      