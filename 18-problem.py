n , target = map(int, input().split())
sum = 1
while True:
    if n == target:
      print(sum)
      break
    
    elif str(target)[-1] == '1':
      target =target//10
      sum+=1
     
    elif n > target:
      print(-1)
      break
    
    elif target%2==0:
      target=target//2
      sum+=1
    else:
      print(-1)
      break
      

