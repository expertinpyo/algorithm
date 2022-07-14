import sys
sys.stdin = open('input.txt')

def dfs(x, cnt):
    global ans
    ans = max(ans, cnt)
    for y in dic[x]:
        if not visited[y]:
            visited[y] = 1
            dfs(y, cnt + 1)
            visited[y] = 0

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    dic = dict()
    for i in range(m):
        key, value = arr[i][0], arr[i][1]
        if key in dic:
            dic[key] += [value]
        else:
            dic[key] = [value]
        if value in dic:
            dic[value] += [key]
        else:
            dic[value] = [key]
    ans = 1
    visited = [0] * (n + 1)
    if dic:
        for key in dic:
            visited[key] = 1
            dfs(key, 1)
            visited[key] = 0
    print(f"#{tc} {ans}")

