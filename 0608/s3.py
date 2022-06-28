# 13460
# 세로 n 가로 m
# 빨간 구슬을 구멍을 통해서 빼내는 것
# 파란 구슬이 구멍에 들어가면 안된다.
from collections import deque

def bfs(cal):
    queue = deque()
    queue.append(cal)
    visited[cal[0]][cal[1]] = -1
    while queue:
        x, y = queue.popleft()
        for d in di:
            new_x, new_y = x + d[0], y + d[1]
            if 1 <= new_x < n-1 and 1 <= new_y < m-1:
                if arr[new_x][new_y] != '#' and not visited[new_x][new_y]:
                    if visited[x][y] == -1:
                        d_list.append(d[2])
                        cnt = 1
                    else:
                        cnt = visited[x][y][1]
                        if visited[x][y][0] != d[2]:
                            d_list.append(d[2])
                            cnt += 1
                    queue.append([new_x, new_y])
                    visited[new_x][new_y] = (d[2], cnt)


n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(input()))

di = [[1, 0, 1], [0, 1, 2], [-1, 0, 3], [0, -1, 4]]
visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            red = [i, j]
        elif arr[i][j] == 'B':
            blue = [i, j]
        elif arr[i][j] == 'O':
            end = [i, j]
d_list = []
bfs(red)
print(visited)