# r g b  중 하나 칠한 그림 있음
# 그림은 몇개의 구역으로 나눠있음
# 구역은 같은 색깔
# 같은 색상이 상하좌우로 인접해 있는 경우 두 글자는 같은 구역에 속한다
import sys
sys.setrecursionlimit(10**6)

def color(x, y):
    visited[x][y] = 1
    for d in di:
        nx, ny = x + d[1], y + d[0]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and arr[nx][ny] == c:
                color(nx, ny)
    return


def blind(x, y):
    b_visited[x][y] = 1
    for d in di:
        nx, ny = x + d[1], y + d[0]
        if 0 <= nx < n and 0 <= ny < n and not b_visited[nx][ny]:
            if b == 'B':
                if arr[nx][ny] == b:
                    blind(nx, ny)
            else:
                if arr[nx][ny] != 'B':
                    blind(nx, ny)


di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
b_visited = [[0]*n for _ in range(n)]
ans = 0
bns = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            c = arr[i][j]
            color(i, j)
            ans += 1
        if not b_visited[i][j]:
            b = arr[i][j]
            blind(i, j)
            bns += 1
print(ans, bns)