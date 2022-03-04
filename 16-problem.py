n = input()
one = []
zero = []
for i in n.split('1'):
  if i == '':
    continue
  zero.append(i)

for i in n.split('0'):
  if i == '':
    continue
  one.append(i)

if len(one)>len(zero): 
  print(len(zero))  
else:
  print(len(one)) 
  
  