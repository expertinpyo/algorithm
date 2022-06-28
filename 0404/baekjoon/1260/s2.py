def dfs(x):
    visited1[x] = 1
    print(x, end=' ')
    for i in range(1, n+1):
        if not visited1[i] and arr[x][i]:
            dfs(i)



def bfs(x):
    queue = []
    queue.append(x)
    visited2[x] = 1
    while queue:
        x = queue.pop(0)
        print(x, end=' ')
        for i in range(1, n+1):
            if arr[x][i] and not visited2[i]:
                queue.append(i)
                visited2[i] = 1

n, m, v = map(int, input().split())
arr = [[0] * (1+n) for _ in range(n+1)]
for _ in range(m):
    start, end = map(int,input().split())
    arr[start][end] = arr[end][start] = 1

visited1 = [0]*(n+1)
visited2 = [0]*(n+1)
dfs(v)
print()
bfs(v)