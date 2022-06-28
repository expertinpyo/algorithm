# 인접한 4 방향
# 공기청정기 있거나 칸이 없으면 방향으로 확산X
# Arc - (Arc/5) * 확산 방향

from copy import deepcopy

r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
copied = deepcopy(arr)

for i in range(r):
    if arr[i][0]:
        air, bir = i, i+1
        break

ans = 0
while t:
    t -= 1
    for i in range(air, -1, -1):
        if i == air:
            for j in range(c-1, 1, -1):
                copied[i][j] = copied[i][j-1]
            copied[i][1] = 0
        elif i == 0:
            for j in range(c-1):
                copied[i][j] = copied[i][j+1]
            copied[0][-1] = copied[1][-1]
        else:
            copied[i][-1] = arr[i+1][-1]
            copied[i][0] = arr[i-1][0]

    for i in range(bir, r, 1):
        if i == bir:
            for j in range(c-1, 1, -1):
                copied[i][j] = copied[i][j-1]
            copied[i][1] = 0
        elif i == r-1:
            for j in range(c-1):
                copied[i][j] = copied[i][j+1]
            copied[r-1][-1] = copied[r-2][-1]
        else:
            copied[i][-1] = arr[i-1][-1]
            copied[i][0] = arr[i+1][0]
    for i in range(r):
        ans += sum(copied[i])
print(ans)