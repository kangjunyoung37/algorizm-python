import sys
a = int(sys.stdin.readline())
mountain  = list(map(int, sys.stdin.readline().split()))
max = 0
for i in range(a-1):
  a = 0
  for j in mountain[i+1:]:
    if mountain[i]>j:
      a+=1
    else:
      break
  if max < a:
    max = a
print(max)
  

    

  

  
  
  
  
  
 




  

          
          
        
        
      

          

        
     
        
        
        


