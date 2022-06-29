def dfs(x, y, cnt_y, cnt_s):
    global ans
    if cnt_y > 3:
        return
    if cnt_y + cnt_s == 7:
        ans += 1
        return
    for d in di:
        nx, ny = d[1] + x, d[0] + y
        if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
            visited[nx][ny] = 1
            if arr[nx][ny] == 'Y':
                dfs(nx, ny, cnt_y+1, cnt_s)
            else:
                dfs(nx, ny, cnt_y, cnt_s+1)

di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
arr = [list(input()) for _ in range(5)]
ans = 0
for i in range(5):
    for j in range(5):
        visited = [[0] * 5 for _ in range(5)]
        visited[i][j] = 1
        if arr[i][j] == 'Y':
            dfs(i, j, 1, 0)
        else:
            dfs(i, j, 0, 1)
print(ans)