import sys
a = int(sys.stdin.readline())
tree  = list(map(int, sys.stdin.readline().split()))
tree.sort()
for i in range(1,a+1):
  tree[i-1]-=i
result = max(tree)+i+2
print(result)