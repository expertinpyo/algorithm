# 이 코드를 버리는 이유, visited로 모든 경우를 다 돌기에는 경우가 너무너무너무너무 많다.

import sys
sys.stdin = open('input.txt')

def chess(x, y, trial):
    global ans
    if trial == n:
        ans += 1
        return
    for i in range(n):
        if not visited[i][y]:
            visited[i][y] = -1
        if not visited[x][i]:
            visited[x][i] = -1
        if x+i < n and y+i < n and not visited[x+i][y+i]:
            visited[x+i][y+i] = -1
        if 0 <= x-i and 0 <= y-i and not visited[x-i][y-i]:
            visited[x-i][y-i] = -1
        if 0 <= x-i and 0 <= y-i and not visited[x-i][y-i]:
            visited[x-i][y-i] = -1
        if x+i < n and 0 <= y-i and not visited[x+i][y-i]:
            visited[x+i][y-i] = -1
        if 0 <= x-i and y+i < n and not visited[x-i][y+i]:
            visited[x-i][y+i] = -1
    for i in range(n):
        if not visited[trial][i]:
            visited[trial][i] = 1
            chess(trial, i, trial+1)
            visited[trial][i] = 0



T = int(input())
for tc in range(1, T+1):
    n = int(input())
    if n == 1:
        ans = 1
    else:
        for i in range(n):
            visited[0]
    print(f"#{tc} {ans}")