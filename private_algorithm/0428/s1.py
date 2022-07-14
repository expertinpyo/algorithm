from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    cnt = 0
    di1 = False
    while queue:
        x, y = queue.popleft()
        if arr[x][y] == 'O':
            return cnt
        if cnt == 10:
            return 11
        for d in di:
            nx, ny = x + d[1], y + d[0]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == '.' and not visited[nx][ny]:
                if not di1:
                    di1 = d
                else:
                    if di1 != d:
                        di1 = d
                        cnt += 1
                visited[nx][ny] = 1
                queue.append([nx, ny])

    return 11


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
    cnt = bfs(c[0], c[1])
    if c[0] == rx and cnt > 10:
        if cnt > 10:
            ans = -1
            break
        else:
            ans = min(cnt, ans)
    else:
        if cnt <= ans:
            ans = -1

print(ans)
