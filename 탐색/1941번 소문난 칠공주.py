import sys
a = []
for i in range(5):
  a += list(map(str,sys.stdin.readline().rstrip()))
dx = [0,1,0,-1]
dy = [1,0,-1,0]
check= [[0]*5 for _ in range(5)]
visit = [0] * 25
result = 0
def check_list(s,position):
  x = s//5
  y = s%5
  check[x][y] = 1
  for i in range(4):
    cdx = x+dx[i]
    cdy = y+dy[i]
    if cdx<0 or cdy<0 or cdx >= 5 or cdy >= 5:
      continue
    b = cdx*5 + cdy 
    if check[cdx][cdy]== 0 and b in position:
      check[cdx][cdy] = 1
      check_list(b,position)

def calculate(index,stack,position):
  global result
  global check 
  if stack.count('Y') > 3:
    return
  if index == 7:
    check_list(position[0],position)
    if sum(sum(check, [])) == 7:
      result+=1
    check = [[0]*5 for _ in range(5)]
    return
  for i in range(25):
    if visit[i] == 0:
      visit[i] = 1
      calculate(index+1,stack+a[i],position+[i])
      for j in range(i+1,25):
        visit[j] = 0
calculate(0,"",[])
print(result)



    
  