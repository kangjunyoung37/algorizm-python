import sys
a , b = map(int,sys.stdin.readline().split())
la = [list(map(int,sys.stdin.readline().rstrip('\n'))) for _ in range(a)]
lb = [list(map(int,sys.stdin.readline().rstrip('\n'))) for _ in range(a)]
result = 0
def chage(row,colunm):
  for i in range(3):
    for j in range(3):
      if la[row+i][colunm+j] == 1:
        la[row+i][colunm+j] = 0
      elif la[row+i][colunm+j] == 0:
        la[row+i][colunm+j] = 1
     
for i in range(a-2):
  for j in range(b-2):
    if la[i][j] != lb[i][j]:
      chage(i,j)
      result+=1
    elif la[i][j] == lb[i][j]:
      continue
if la==lb:
  print(result)
else:
  print(-1)
    

    