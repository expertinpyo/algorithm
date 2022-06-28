import sys
sys.stdin = open('input.txt')

def mmm(x):
    global ans
    if x == n:
        return
    if x == 0:
        min_num = min(arr[x])
        idx = arr[x].index(min_num)
        visited[x][idx] = 1
        ans += min_num
    else:
        min_num = min(arr[x])
        idx = arr[x].index(min_num)
        cnt = 0
        for i in range(n):
            if not visited[i][idx]:
                cnt += 1
            else: break
        if cnt == n:
            visited[x][idx] = 1
            ans += min_num
        else:
            arr[x][idx] = 10
            mmm(x)
    mmm(x+1)

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    ans = 0
    for i in range(n):
        if arr[0][i] == min(arr[i]):
            mmm(0)
    print(f'#{tc} {ans}')
