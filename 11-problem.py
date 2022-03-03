n = int(input())
a = 1
sum = 0
while True:
  if sum > n:
    print(a-2)
    break
  elif sum == n:
    print(a-1)
    break
  sum += a
  a+=1