import sys
sys.stdin = open('input.txt')

def dfs(x, y):
    global ans
    for direction in range(4):
        nx = x + di[direction]
        ny = y + dj[direction]
        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] == 3:
                ans = 1
                return
            if not arr[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                dfs(nx, ny)

T = int(input())
for tc in range(1, T+1):

    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    ans = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                dfs(i, j)

    print(f"#{tc} {ans}")
