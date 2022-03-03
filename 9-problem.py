food = int(input())
time = [300,60,10]
sum = [0]*3
for i in range(3):
  sum[i] = food//time[i]
  food%=time[i]
if food != 0:
  print(-1)
else: 
  for i in range(3):
    print(sum[i],end=" ")
    