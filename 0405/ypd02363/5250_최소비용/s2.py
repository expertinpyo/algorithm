from collections import deque
import sys
sys.stdin = open('input.txt')

def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()
        for d in di:
            nx, ny = x + d[1], y + d[0]
            if 0 <= nx < n and 0 <= ny < n:
                s = visited[x][y] + 1
                if arr[nx][ny] > arr[x][y]:
                    s += arr[nx][ny] - arr[x][y]
                if s < visited[nx][ny]:
                    visited[nx][ny] = s
                    queue.append([nx, ny])
            # if visited[nx][ny] > visited[x][y] + abs(arr[nx][ny] - arr[x][y]):
            #     visited[nx][ny] = visited[x][y] + 1 + abs(arr[nx][ny] - arr[x][y])
            #     queue.append([nx, ny])

di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[10**6] * n for _ in range(n)]
    visited[0][0] = 0
    bfs(0, 0)
    print(f"#{tc} {visited[-1][-1]}")