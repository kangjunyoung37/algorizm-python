a = input()
b = input()
i = 0
count = 0
while i <=len(a)-len(b):
  
  if a[i:i+len(b)]==b:
    count+=1
    i+=len(b)
  else:
    i+=1
print(count)