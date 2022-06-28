# 19238
from collections import deque

def taxi(dx, dy, fuels):
    fuel = fuels
    cnt = 0
    x, y = dx-1, dy-1
    while cnt < m:
        if fuel < 0:
            fuel = -1
            break

        visited = move(x, y)
        distance = 10**6
        for i in range(m):
            px, py = passangers[i][0]-1, passangers[i][1]-1
            if arr[px][py] != -1:
                if visited[px][py] == -1:
                    fuel = -1
                    break
                else:
                    if visited[px][py] < distance:
                        distance = visited[px][py]
                        idx = i
                    elif visited[px][py] == distance:
                        idxpx, idxpy = passangers[idx][0]-1, passangers[idx][1]-1
                        if px < idxpx:
                            distance = visited[px][py]
                            idx = i
                        elif px == idxpx:
                            if py < idxpy:
                                distance = visited[px][py]
                                idx = i

        if fuel < 0 or fuel < distance:
            fuel = -1
            break

        fuel -= distance

        x, y = passangers[idx][0]-1, passangers[idx][1]-1
        px, py = passangers[idx][2]-1, passangers[idx][3]-1

        arr[x][y] = -1

        visited2 = move(x, y)
        destination = visited2[px][py]

        if destination == -1 or fuel < destination:
            fuel = -1
            break

        fuel += destination
        cnt += 1
        x, y = px, py

    print(fuel)


def move(x, y):
    queue = deque()
    queue.append([x, y])
    visited = [[-1] * n for _ in range(n)]
    visited[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + di[i][1], y + di[i][0]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] < 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])
    return visited



di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
n, m, fuels = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx, dy = map(int, input().split())
passangers = [list(map(int,input().split())) for _ in range(m)]

taxi(dx, dy, fuels)