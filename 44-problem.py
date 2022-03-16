import sys
a = int(sys.stdin.readline())
krain = list(map(int, sys.stdin.readline().split()))

box = int(sys.stdin.readline())
weight = list(map(int, sys.stdin.readline().split()))

krain.sort(reverse=True)
weight.sort(reverse=True)
count = 0
if krain[0]<weight[0]:
  print(-1)
else:
  while len(weight)>0:
    for i in krain:
      for j in range(len(weight)):
        if i >=weight[j]:
          del weight[j]
          break
    count+=1    
  print(count)       
  
 




  

          
          
        
        
      

          

        
     
        
        
        


