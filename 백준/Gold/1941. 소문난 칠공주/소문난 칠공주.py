from itertools import combinations as cb
from collections import deque

def bfs(c):
    queue = deque([c.pop()])
    while queue:
        x, y = queue.popleft()
        for d in di:
            nx, ny = d[0] + x, d[1] + y
            if (nx, ny) in c:
                c.remove((nx, ny))
                queue += (nx, ny),
    return not c

arr = [list(input()) for _ in range(5)]
cbs = cb(set((i, j) for i in range(5) for j in range(5)), 7)
di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
ans = 0
for c in cbs:
    cnt_y = 0
    for i, j in c:
        if arr[i][j] == 'Y':
            cnt_y += 1
        if cnt_y > 3:
            break
    if cnt_y > 3:
        continue
    ans += bfs(set(c))
print(ans)