def dfs(x, y, depth, amt):
    global ans
    if depth == 4:
        ans = max(amt, ans)
        return
    if (4-depth) * max_n + amt < ans:
        return

    for d in di:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if depth <= 2:
                visited[nx][ny] = 1
                dfs(x, y, depth + 1, amt + arr[nx][ny])
                visited[nx][ny] = 0

            visited[nx][ny] = 1
            dfs(nx, ny, depth + 1, amt + arr[nx][ny])
            visited[nx][ny] = 0

di =[[0, 1], [1, 0], [-1, 0], [0, -1]]
N, M = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

ans = 0
visited = [[0] * M for _ in range(N)]

max_n = 0
for i in range(N):
    max_n = max(max_n, max(arr[i]))

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 1, arr[i][j])
        visited[i][j] = 0
print(ans)