from itertools import combinations as cb
from collections import deque

arr = [list(input()) for _ in range(5)]
cbs = list(cb(range(25), 7))
di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
ans = 0
for c in cbs:
    cnt_y = 0
    fail = False
    for i in c:
        a, b = i // 5, i % 5
        if arr[a][b] == 'Y':
            cnt_y += 1
        if cnt_y > 3:
            fail = True
            break
    if not fail:
        visited = [[0] * 5 for _ in range(5)]
        for i in c:
            a, b = i // 5, i % 5
            visited[a][b] = 1
        queue = deque([(a, b)])
        check = 1
        visited[a][b] = 0
        while queue:
            x, y = queue.popleft()
            for d in di:
                nx, ny = d[0] + x, d[1] + y
                if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = 0
                    check += 1
        if check == 7:
            ans += 1
print(ans)