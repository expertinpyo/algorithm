# 인접한 4 방향
# 공기청정기 있거나 칸이 없으면 방향으로 확산X
# Arc - (Arc/5) * 확산 방향

from copy import deepcopy

r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]


for i in range(r):
    if arr[i][0]:
        air, bir = i, i+1
        break
di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
ans = 0
while t:
    t -= 1
    copied = deepcopy(arr)
    for i in range(r):
        for j in range(c):
            if copied[i][j] >= 5:
                cnt = 0
                for d in di:
                    ni, nj = i + d[1], j + d[0]
                    if 0 <= ni < r and 0 <= nj < c and copied[ni][nj] != -1:
                        arr[ni][nj] += copied[i][j] // 5
                        cnt += 1
                arr[i][j] -= (copied[i][j]//5)*cnt

    # 공기청정기 순환
    for i in range(air-1, 0, -1):
        arr[i][0] = arr[i-1][0]
    for i in range(c-1):
        arr[0][i] = arr[0][i+1]
    for i in range(0, air, 1):
        arr[i][-1] = arr[i+1][-1]
    for i in range(c-1, 1, -1):
        arr[air][i] = arr[air][i-1]
    arr[air][1] = 0

    for i in range(bir+1, r-1, 1):
        arr[i][0] = arr[i+1][0]
    for i in range(c-1):
        arr[r-1][i] = arr[r-1][i+1]
    for i in range(r-1, bir, -1):
        arr[i][-1] = arr[i-1][-1]
    for i in range(c-1, 1, -1):
        arr[bir][i] = arr[bir][i-1]
    arr[bir][1] = 0

for i in range(r):
    ans += sum(arr[i])

ans += 2

print(ans)