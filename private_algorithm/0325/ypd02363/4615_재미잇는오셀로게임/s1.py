import sys
sys.stdin = open('input.txt')

def dfs(x, y, c):
    for i in range(8):
        nx = x + delta[i][1]
        ny = y + delta[i][0]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != c:
            arr[nx][ny] = arr[x][y] = c

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [[0]*n for _ in range(n)]
    arr[n//2-1][n//2-1] = arr[n//2][n//2] = 2
    arr[n//2-1][n//2] = arr[n//2][n//2-1] = 1
    delta = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1],[0, -1], [1, -1]]
    for trial in range(m):
        y, x, c = map(int, input().split())
        dfs(x-1, y-1, c)
    print(arr)