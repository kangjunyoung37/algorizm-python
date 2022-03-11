from collections import Counter
import sys
n = list(sys.stdin.readline().rstrip())
sortn = sorted(n)
count = dict(Counter(sortn))
result =[]
odd = []
if len(sortn)%2==0:
  for alpa in count:
    count[alpa]/=2
    for _ in range(int(count[alpa])):
      result.append(alpa)
  ans = "".join(result+result[::-1])
  if len(ans)==len(sortn):
    print(ans)
  else:
    print("I'm Sorry Hansoo")

elif len(sortn)%2==1:
  cnt = 0
  for alpa in count:
    if count[alpa] %2 == 1:
      odd.append(alpa)
      cnt+=1
    count[alpa]/=2
    for _ in range(int(count[alpa])):
      result.append(alpa)
  ans = "".join(result+odd+result[::-1])
  if cnt >=2:
    print("I'm Sorry Hansoo")
  elif len(ans) == len(sortn):
    print(ans)
  else:
    print("I'm Sorry Hansoo")
    
  