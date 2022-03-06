n = int(input())
positive = []
negative = []
onelist = []
result = 0
for _ in range(n):
  a = int(input())
  if a > 1:
    positive.append(a)
  elif a <= 0:
    negative.append(a)
  else:
    onelist.append(a)
positive.sort(reverse = True)
negative.sort()

if len(positive) % 2 == 0:
  for i in range(0,len(positive),2):
      result += positive[i]*positive[i+1]
else:
  for i in range(0,len(positive)-1,2):
      result += positive[i]*positive[i+1]
  result += positive[len(positive)-1]

if len(negative) % 2 == 0:
  for i in range(0,len(negative),2):
      result += negative[i]*negative[i+1]
else:
  for i in range(0,len(negative)-1,2):
      result += negative[i]*negative[i+1] + negative[-1]
  result += negative[len(negative)-1]  
result += sum(onelist)
print(result)  