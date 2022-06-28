import sys
sys.stdin = open('input.txt')
# dp로 해보자
def dfs(key, num):
    global ans
    if visited[key]:
        ans = max(num, ans)
        return

    visited[key] = 1
    for v in dic[key]:
        dfs(v, num+1)



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
    if dic:
        dp = [0]*(n+1)
        for key in dic:
            visited = [0]*(n+1)
            dfs(key, 0)

    print(f"#{tc} {ans}")