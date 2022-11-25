from collections import deque
from copy import deepcopy
def bfs(x, y):
    global ans
    queue = deque([(x, y, 1, arr[x][y], [(x, y)])])

    while queue:
        x, y, length, amt, route = queue.popleft()
        if length == 4:
            ans = max(ans, amt)
        if (4-length) * max_n + amt < ans:
            continue
        for d in di:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in route:
                new_route = deepcopy(route)
                new_route.append((nx, ny))
                queue.append((nx, ny, length + 1, amt + arr[nx][ny],new_route ))
                if length <= 2:
                    for d2 in di:
                        nnx, nny = x + d2[0], y + d2[1]
                        if 0 <= nnx < N and 0 <= nny < M and (nnx, nny) not in new_route:
                            new_route2 = deepcopy(new_route)
                            new_route2.append((nnx, nny))
                            queue.append((nnx, nny, length + 2, amt + arr[nx][ny] + arr[nnx][nny], new_route2))


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
        if not visited[i][j]:
            bfs(i, j)
            visited[i][j] = 1
print(ans)