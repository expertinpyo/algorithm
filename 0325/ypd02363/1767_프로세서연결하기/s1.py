import sys
sys.stdin = open('input.txt')

def dfs(x, y):
    for di in range(4):
        for k in range(1, n):
            nx = x + delta[di][1]*k
            ny = y + delta[di][0]*k
            if 0 <= nx < n and 0 <= ny < n and not arr[nx][ny]:
                arr[nx][ny] = 2
            else:
                break


delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    for i in range(1, n-1):
        for j in range(1, n-1):
            if arr[i][j] == 1:
                dfs(i, j)