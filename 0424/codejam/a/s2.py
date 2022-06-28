from copy import deepcopy as dc
def dfs(lidx, ridx, max_num, cnt):
    global ans
    if lidx == n // 2  or ridx == n // 2 :
        ans = max(ans, cnt)
        return

    left, right = arr[lidx], arr[ridx]

    if left >= max_num:
        dfs(lidx + 1, ridx, max(max_num, left), cnt + 1)
    if right >= max_num:
        dfs(lidx, ridx-1, max(max_num, right), cnt + 1)


T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    max_num = 0
    ans = 0
    lidx = 0
    ridx = -1
    dfs(lidx, ridx, 0, 0)
    print(f'Case #{tc}: {ans}')