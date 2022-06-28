import sys
from collections import deque


sys.stdin = open('input.txt')

def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()
        for d in di:
            nx, ny = x + d[1], y + d[0]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] > visited[x][y] + arr[nx][ny]:
                    visited[nx][ny] = visited[x][y] + arr[nx][ny]
                    queue.append([nx, ny])

di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    visited = [[10**6]*n for _ in range(n)]
    visited[0][0] = 0
    bfs(0, 0)
    print(f"#{tc} {visited[-1][-1]}")