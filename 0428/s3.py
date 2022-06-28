n, m = map(int, input().split())
arr = [list(input()) for _ in range(m)]

def possible(x, y, direction):
    for i in range(1, max(n, m)):
        if direction == 0:
            nx, ny = x, y + i
        elif direction == 1:
            nx, ny = x + i, y
        elif direction == 2:
            nx, ny = x, y - i
        else:
            nx, ny = x - i, y
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == '.':
                continue
            else:
                if direction == 0:
                    ny -= 1
                elif direction == 1:
                    nx -= 1
                elif direction == 2:
                    ny += 1
                else:
                    nx += 1
                return nx, ny



di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            rx, ry = i, j
        elif arr[i][j] == 'B':
            bx, by = i, j

world = [[0]*m for _ in range(n)]
while True:
    for i in range(4):
        rrx, rry = rx + di[i][1], ry - di[i][0]
        if arr[rrx][rry] == '.':
            nrx, nry = possible(rx, ry)
            world[nrx][nry] = 'R'
            world[rx][ry] = 0
            rx, ry = nrx, nry

        # nrx, nry = possible(rx, ry)
        # world[nrx][nry] = 'R'
        # world[rx][ry] = 0

