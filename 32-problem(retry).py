import sys
a , b = map(int,sys.stdin.readline().split())
scedule = list(map(int,sys.stdin.readline().split()))
concent = []
count = 0
temp = 0
tempc = 0
for i in range(b):
  if len(concent)<a and scedule[i] not in concent:
    concent.append(scedule[i])
  elif scedule[i] in concent:
    continue
  else:
    
    for j in concent:
      
      if j not in scedule[i:]:
        tempc = j
        break      
      
      elif temp <= scedule[i:].index(j):
          temp = scedule[i:].index(j)
          tempc = j          
        
    concent[concent.index(tempc)] = scedule[i]
    count +=1
    temp = tempc = 0
    
print(count)