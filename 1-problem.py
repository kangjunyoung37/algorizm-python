n = int(input())
a = 0
while True:

  if n==0:
    break
    
  elif n==3 or n==6 or n==9 or n==12:
    n-=3
    a+=1
    continue    
  elif n<0:
    a = -1
    break  
  
  n-=5
  a+=1
  
print(a)   
