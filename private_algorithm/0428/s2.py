def dfs(x, y, direction):
    global cnt, end, total
    if arr[x][y] == 'O':
        end = True
        return
    if cnt == 10:
        end = True
        cnt = 11
        return
    for i in range(4):
        nx, ny = x + di[i][1], y + di[i][0]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != '#' and not visited[nx][ny]:
            if not i == direction:
                cnt += 1
                direction = i
            visited[nx][ny] = 1
            total += 1
            dfs(nx, ny, direction)
            if end:
                return
            total -= 1
    cnt = 11
    return

di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            rx, ry = i, j
        elif arr[i][j] == 'B':
            bx, by = i, j

ans = 10**6
for c in [[rx, ry], [bx, by]]:
    visited = [[0]*m for _ in range(n)]
    visited[c[0]][c[1]] = 1
    turn = True
    cnt = 0
    end = False
    total = 0
    dfs(c[0], c[1], -1)
    if c[0] == rx and c[1] == ry:
        if cnt > 10:
            ans = -1
            break
        else:
            ans = min(cnt, ans)
            total1 = total
    else:
        if cnt == ans:
            if total <= total1:
                ans = -1
        elif cnt < ans:
            ans = -1

print(ans)
