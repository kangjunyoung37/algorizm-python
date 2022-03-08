import sys
n = int(sys.stdin.readline())
score=[]
for _ in range(n):
  a = int(sys.stdin.readline())
  score.append(a)
temp = 0 
for i in range(-1,-n,-1):
  if score[i]<=score[i-1]:
    temp+=(score[i-1]-(score[i]-1))
    score[i-1]=(score[i]-1)
print(temp)    
  
