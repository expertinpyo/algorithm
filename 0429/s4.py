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
        distance = 10**6
        for i in range(m):  # 승객별 거리 비교
            px, py = passangers[i][0]-1, passangers[i][1]-1
            if arr[px][py] != -1:   # 방문하지 않은 승객이라면
                length = move(x, y, px, py)
                if length == -100:  # 택시가 갈 수 없는 경우
                    fuel = -1
                    break
                else:
                    if length < distance:
                        distance = length
                        idx = i
                    elif length == distance:
                        qx, qy = passangers[idx][0]-1, passangers[idx][1]-1
                        if px < qx:
                            distance = length
                            idx = i
                        elif px == qx:
                            if py < qy:
                                distance = length
                                idx = i
        if fuel < 0 or fuel < distance:
            fuel = -1
            break

        fuel -= distance

        x, y = passangers[idx][0]-1, passangers[idx][1]-1
        px, py = passangers[idx][2]-1, passangers[idx][3]-1

        arr[x][y] = -1

        consume = move(x, y, px, py)

        if consume < 0 or fuel < consume:
            fuel = -1
            break

        fuel += consume
        cnt += 1
        x, y = px, py

    print(fuel)


def move(x, y, px, py):
    queue = deque()
    queue.append([px, py])
    visited = [[0] * n for _ in range(n)]
    while queue:
        px, py = queue.popleft()
        if px == x and py == y:
            return visited[px][py]
        for i in range(4):
            nx, ny = px + di[i][1], py + di[i][0]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] < 1 and not visited[nx][ny]:
                visited[nx][ny] = visited[px][py] + 1
                queue.append([nx, ny])
    return -100 # 그 곳에 갈 수 없는 경우

di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
n, m, fuels = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx, dy = map(int, input().split())
passangers = [list(map(int,input().split())) for _ in range(m)]

taxi(dx, dy, fuels)