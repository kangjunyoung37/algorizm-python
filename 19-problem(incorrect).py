dia , bag = map(int,input().split())
diaimpo = [list(map(int, input().split())) for _ in range(dia)]
bagimpo = []
sum = 0
for _ in range(bag):
  a = int(input())
  bagimpo.append(a)
diaimpo = sorted(diaimpo,key = lambda x:x[1],reverse = True)
bagimpo.sort()
for i in bagimpo:
  for j in range(len(diaimpo)):
    w,p = diaimpo[j]
    if i >= w:
      diaimpo.pop(j)
      sum+=p
      break
      
print(sum)