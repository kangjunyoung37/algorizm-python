n = int(input())
dice = list(map(int,input().split()))
arr = [min(dice[0],dice[5]),min(dice[1],dice[4]),min(dice[2],dice[3])]
arr.sort()
result = 0
if n==1:
  result = sum(dice)-max(dice)
else:
  a3 = sum(arr)
  a2 = arr[0]+arr[1]
  a1 = arr[0]
  n1 = (n-1) * (n-2) * 4 + (n-2) * (n-2);
  n2 = (n-1) * 4 + (n-2) * 4;
  n3 = 4
  result+= a1*n1
  result+= a2*n2
  result+= a3*n3


print(result)