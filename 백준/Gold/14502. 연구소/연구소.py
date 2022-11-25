from itertools import combinations as cb
from collections import deque

di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
ans = 0
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus.append([i, j])
walls = []
for i in range(N):
    for j in range(M):
        walls.append((i, j))
idxs = list(cb(walls, 3))
for idx in idxs:
    ok = False
    for i in range(3):
        if arr[idx[i][0]][idx[i][1]]:
            ok = True
            break
    if ok:
        continue

    for i in range(3):
        arr[idx[i][0]][idx[i][1]] = 1

    visited = [[0] * M for _ in range(N)]
    for v in virus:
        if not visited[v[0]][v[1]]:
            queue = deque([(v[0], v[1])])
            visited[v[0]][v[1]] = 1
            while queue:
                x, y = queue.popleft()
                for d in di:
                    nx, ny = x + d[0], y + d[1]
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[nx][ny] != 1:
                        visited[nx][ny] = 1
                        queue.append((nx, ny))
    cnt = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and not arr[i][j]:
                cnt += 1

    ans = max(ans, cnt)

    for i in range(3):
        arr[idx[i][0]][idx[i][1]] = 0

print(ans)