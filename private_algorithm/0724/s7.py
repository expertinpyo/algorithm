# 17299
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
dic = {}
arrs = [0] * N
for i in range(N):
    if arr[i] not in dic:
        dic[arr[i]] = 1
    else:
        dic[arr[i]] += 1
for i in range(N):
    arrs[i] = dic[arr[i]]
ans = [-1] * N
stack = [0]
for i in range(N-1, -1, -1):
    while stack and arrs[stack[-1]] < arrs[i]:
        ans[stack.pop()] = arr[i]
    stack.append(i)
print(*ans)