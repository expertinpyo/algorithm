# 17298 based on stack
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
stack = [0]
ans = [-1] * N

for i in range(1, N):
    while stack and arr[stack[-1]] < arr[i]:
        ans[stack.pop()] = arr[i]
    stack.append(i)
print(*ans)