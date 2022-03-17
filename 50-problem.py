import sys
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort()
print(A[(n-1)//2])