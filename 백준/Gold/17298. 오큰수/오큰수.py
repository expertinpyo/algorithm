N = int(input())
arr = list(map(int,input().split()))
stack = [arr[-1]]
ans = [-1] * N
for i in range(N-2, -1, -1):
    while stack:
        if arr[i] < stack[-1]:
            ans[i] = stack[-1]
            break
        stack.pop()
    stack.append(arr[i])
print(*ans)