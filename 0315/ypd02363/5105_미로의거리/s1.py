# 최소 몇개 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내자

import sys
sys.stdin = open('input.txt')

def bfs(x, y):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    queue = [[x, y]]
    while queue:
        x, y = queue.pop(0)
        for direction in range(4):
            nx = x + di[direction]
            ny = y + dj[direction]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if arr[nx][ny] == 0:
                    queue.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
                if arr[nx][ny] == 3:
                    visited[nx][ny] = visited[x][y]
                    return visited[nx][ny]
    return 0

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                print(f"#{tc} {bfs(i, j)}")
