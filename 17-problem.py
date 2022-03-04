n = []
while True:
  camp,campvaca,myvaca = map(int, input().split())
  if camp==0 and campvaca==0 and myvaca==0:
    break
  else:
    n.append([camp,campvaca,myvaca])
a = 1
for i in n:
  camp,campvaca,myvaca = i
  sum = 0
  sum += camp*(myvaca//campvaca)
  if myvaca%campvaca > camp:
    sum+=camp
  else:
    sum+=(myvaca%campvaca)
    
  print("Case "+str(a)+":",sum) 
  a+=1

  
    
    