from itertools import combinations as cb
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus = []
zero = 0
di = [[1, 0], [0, 1], [-1, 0], [0, -1]]

for i in range(N):
    for j in range(N):
        if arr[i][j] != 1:
            if arr[i][j] == 2:
                virus.append((i, j))
            else:
                zero += 1

if not zero:
    print(0)
    exit()

idxs = list(cb(virus, M))
ans = 10 ** 9
for idx in idxs:
    queue = deque([])
    visited = [[0] * N for _ in range(N)]
    for x, y in idx:
        queue.append((x, y, 0))
        visited[x][y] = 1   # 첫 시작 좌표 설정

    cnt = 0
    while queue:
        x, y, time = queue.popleft()
        cnt = max(time, cnt)
        if cnt >= zero: # 더 점검 할 이유가 없음
            break
        for d in di:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] != 1 and cnt < ans:
                visited[nx][ny] = time + 1
                queue.append((nx, ny, time + 1))

    visit = 0
    minus = True
    for i in range(N):
        for j in range(N):
            if visited[i][j] and not arr[i][j]:
                visit += 1
                if cnt == visited[i][j]:
                    minus = False

    if minus:
        cnt -= 1

    if visit >= zero:
        ans = min(cnt, ans)
print(ans) if ans < 10 ** 9 else print(-1)
