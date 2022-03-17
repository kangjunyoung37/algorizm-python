import sys
n = int(sys.stdin.readline())
for _ in range(n):
  A = []
  result = [0]*1001
  sum = 0
  book , student = map(int,sys.stdin.readline().split())
  for _ in range(student):
    a =list(map(int ,sys.stdin.readline().split()))
    A.append(a)
  A = sorted(A, key = lambda x: x[1])
  for a,b in A:
    if result[a]==0:
      result[a] = 1
      sum+=1
    elif result[a]!=0:
      while a <=b:
        if result[a]==0:
          result[a] = 1
          sum+=1
          break
        a+=1
  print(sum)
      
        
        
  

