# 1987
# bfs로 진행하면 될 듯
# 같은 알파벳 적힌 칸은 두번 지날 수 없음
from collections import deque
def bfs():
    global ans
    queue = deque()
    queue.append([0, 0])
    while queue:
        x, y = queue.popleft()
        for d in di:
            nx, ny = x + d[1], y + d[0]
            if 0 <= nx < r and 0 <= ny < c:
                num = ord(arr[nx][ny]) - 65
                if not visited[num]:
                    visited[num] = 1
                    queue.append([nx, ny])
                    ans += 1

di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
visited = [0]*26
r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
visited[ord(arr[0][0])-65] = 1
ans = 1
bfs()
print(ans)