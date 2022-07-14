# 최소 몇개 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내자

import sys
sys.stdin = open('input.txt')


def bfs(x, y):
    queue = [[x, y]]
    while queue:
        x, y = queue.pop(0)
        for direction in range(4):
            nx = x + di[direction]
            ny = y + dj[direction]
            if 0 <= nx < 16 and 0 <= ny < 16 and not visited[nx][ny]:
                if arr[nx][ny] == 0:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1
                if arr[nx][ny] == 3:
                    visited[nx][ny] = 1
                    return 1
    return 0


for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                print(f"#{tc} {bfs(i, j)}")
