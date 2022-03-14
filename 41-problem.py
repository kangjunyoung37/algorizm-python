import sys
a = sys.stdin.readline().rstrip()
result = ''
i = 0
while i<len(a):
  if a[i:i+4] == "XXXX":
    result+="AAAA"
    i+=4
  elif a[i:i+2]=="XX":
    result+="BB"
    i+=2
  else:
    result+=a[i]
    i+=1
if "X" in result:
  print(-1)
else:
  print(result)
                  
    
    
  


    