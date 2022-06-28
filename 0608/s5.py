# 13460
# bfs
# 동시에 움직이는 모델을 생각해보자
# bfs로 red에서 O로 갈 수 있는 가장 빠른 변화점들 파악하고
# 그 변화하는 것을 바탕으로 동시에 red와 blue를 돌려본다
# 갔던 길로 다시 못간다는 말은 없다

# 따라서, 갔던 길로도 당연히 다시 갈 수 있음
# 다만, 최단 경로가 되려면 bfs 탐색으로 이전 경로를 완벽히 숙지하는 것이 옳다.
# 따라서, while문을 조금 수정한다면 옳게 되지 않을까 싶다.

from collections import deque

def bfs(axis):
    queue = deque()
    queue.append(axis)
    while queue:
        x, y = queue.popleft()
        if x == end[0] and y == end[1]:
            break
        for d in di:
            new_x, new_y = x + d[0], y + d[1]
            if 1 <= new_x < n-1 and 1 <= new_y < m-1 and not visited[new_x][new_y] and arr[new_x][new_y] != '#':
                if visited[x][y] == -1:
                    visited[x][y] = d[2]
                    path[x][y] = str(d[2])
                if visited[x][y] != d[2]:
                    visited[x][y] = d[2]
                    path[new_x][new_y] = path[x][y] + str(d[2])
                else:
                    path[new_x][new_y] = path[x][y]
                visited[new_x][new_y] = d[2]
                queue.append([new_x, new_y])

def check(command, red, blue):
    commands = list(map(int, command))
    r = b = False

    for num in commands:
        d = di[num-1]
        while True:
            rx, ry = red
            new_rx, new_ry = rx + d[0], ry + d[1]
            if 1 <= new_rx < n-1 and 1 <= new_ry < m-1 and arr[new_rx][new_ry] not in ['B', '#']:
                if new_rx == end[0] and new_ry == end[1]:
                    r = True
                    arr[rx][ry] = '.'
                    break
                red = new_rx, new_ry
                arr[new_rx][new_ry] = 'R'
                arr[rx][ry] = '.'
            else:
                break
        while True:
            bx, by = blue
            new_bx, new_by = bx + d[0], by + d[1]
            if 1 <= new_bx < n-1 and 1 <= new_by < m-1 and arr[new_bx][new_by] not in ['R', '#']:
                if new_bx == end[0] and new_by == end[1]:
                    b = True
                    arr[bx][by] = '.'
                    break
                blue = new_bx, new_by
                arr[new_bx][new_by] = 'B'
                arr[bx][by] = '.'

            else:
                break

    if r and not b:
        return len(command)
    else:
        return -1

di = [[1, 0, 1], [0, 1, 2], [-1, 0, 3], [0, -1, 4]]
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(input()))
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            red = [i, j]
        elif arr[i][j] == 'B':
            blue = [i, j]
        elif arr[i][j] == 'O':
            end = [i, j]
visited = [[0] * m for _ in range(n)]
path = [[''] * m for _ in range(n)]
visited[red[0]][red[1]] = -1
bfs(red)
print(path[end[0]][end[1]])

if 1 <= len(path[end[0]][end[1]]) < 11:
    print(check(path[end[0]][end[1]], red, blue))
else:
    print(-1)