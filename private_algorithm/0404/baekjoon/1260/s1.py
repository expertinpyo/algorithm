from collections import deque

def dfs(x):
    stack = [x]
    visited = [0]*(n+1)
    visited[x] = 1
    ans = []
    while len(ans) != n:
        x = stack.pop()
        for i in range(1, n+1):
            if arr[x][i] and not visited[i]:
                visited[i] = 1
                stack.append(i)
        stack.sort(reverse=True)
        ans.append(x)

    return ans

n, m, v = map(int, input().split())
arr = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    start, end = map(int, input().split())
    arr[start][end] = arr[end][start] = 1

print(*dfs(v))
# print(bfs(v))