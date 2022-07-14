from copy import deepcopy

r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
di = [[1, 0], [0, 1], [-1, 0], [0, -1]]

for i in range(r):
    if arr[i][0] < 0:
        top = i
        bot = i+1
        break

while t:
    t -= 1

    # 1. 미세먼지 확산
    copy_arr = deepcopy(arr)
    for i in range(r):
        for j in range(c):
            if copy_arr[i][j] >= 5:
                amount = copy_arr[i][j] // 5
                cnt = 0
                for d in di:
                    ni, nj = i + d[1], j + d[0]
                    if 0 <= ni < r and 0 <= nj < c and arr[ni][nj] != -1:
                        arr[ni][nj] += amount
                        cnt += 1
                arr[i][j] -= cnt * amount

    # 2. 공기 청정기 가동
    # 윗 줄 먼저, 반시계방향 회전
    for i in range(top-1, 0, -1):
        arr[i][0] = arr[i-1][0]
    for i in range(c-1):
        arr[0][i] = arr[0][i+1]
    for i in range(top):
        arr[i][c-1] = arr[i+1][c-1]
    for i in range(c-1, 1, -1):
        arr[top][i] = arr[top][i-1]
    arr[top][1] = 0

    # 아랫줄, 시계방향 회전
    for i in range(bot+1, r-1, 1):
        arr[i][0] = arr[i+1][0]
    for i in range(c-1):
        arr[r-1][i] = arr[r-1][i+1]
    for i in range(r-1, bot, -1):
        arr[i][c-1] = arr[i-1][c-1]
    for i in range(c-1, 1, -1):
        arr[bot][i] = arr[bot][i-1]
    arr[bot][1] = 0

ans = 0
for i in range(r):
    ans += sum(arr[i])
ans += 2
print(ans)