import sys
a , b = map(int,sys.stdin.readline().split())
scedule = list(map(int,sys.stdin.readline().split()))
uselist = [0]*(b+1)
concent = []
count = 0
for i in range(b):
  uselist[scedule[i]]+=1

for i in range(a):
  uselist[scedule[i]]-=1
  if scedule[i] in concent:
    continue
  else:
    concent.append(scedule[i])

for i in range(a,b):
  d = []
  uselist[scedule[i]]-=1
  if len(concent)<a and scedule[i] not in concent:
    concent.append(scedule[a])
  elif scedule[i] in concent:
    continue
  else:
    for j in range(a):
      d.append(uselist[scedule[a]])
      del concent[d.index(min(d))]
    concent.append(scedule[i])
    count+=1
    print(concent)
 
print(count)