# 마법사 상어와 토네이도
# N * N

# 토네이도 한 번에 한 칸 이동
# x => y
# y의 모든 모래가 비율과 a가 적혀있는 칸으로 이동함
# a로 이동하는 모래 양 => 비율이 적혀있는 칸으로 이동하지 않은 남은 모래의 양과 동일
# 모래가 이미 있는 칸으로 모래가 이동하면 모래 양은 더해짐
# 격자 밖으로 나간 모래 양을 찾아라
# 모래 양 무조건 0 처음에
# 어차피 반복됨
# 따라서, 공유하는 것을 중요하게 하면 된다.
def sand(x, y, direction):
    total = out = 0
    if not direction % 2: # 좌 / 우
        if direction:
            lot = 1
        else:
            lot = -1
        last_x, last_y = x, y + lot
        five_x, five_y = last_x, last_y + lot
        if 0 <= five_x < N and 0 <= five_y < N:
            arr[five_x][five_y] += int(arr[x][y] * 0.05)
        else:
            out += int(arr[x][y] * 0.05)
        total += int(arr[x][y] * 0.05)
        for i in [-2, -1, 1, 2]:    # 2, 7%
            nx, ny = x + i, y
            if abs(i) == 2:
                first = 0.02
            else:
                first = 0.07
            if 0 <= nx < N and 0 <= ny < N:
                arr[nx][ny] += int(arr[x][y] * first)
            else:
                out += int(arr[x][y] * first)
            total += int(arr[x][y] * first)
        for xx, yy in [[-1, -1], [1, -1]]:
            nx, ny = x + xx, y + yy
            if not direction:
                second = 0.1
            else:
                second = 0.01
            if 0 <= nx < N and 0 <= ny < N:
                arr[nx][ny] += int(arr[x][y] * second)
            else:
                out += int(arr[x][y] * second)
            total += int(arr[x][y] * second)
        for xx, yy in [[1, 1], [-1, 1]]:
            nx, ny = x + xx, y + yy
            if not direction:
                third = 0.01
            else:
                third = 0.1
            if 0 <= nx < N and 0 <= ny < N:
                arr[nx][ny] += int(arr[x][y] * third)
            else:
                out += int(arr[x][y] * third)
            total += int(arr[x][y] * third)

    else:
        if direction == 1:       # 상 / 하
            lot = 1
        else:
            lot = -1
        last_x, last_y = x + lot, y
        five_x, five_y = last_x  + lot, last_y
        if 0 <= five_x < N and 0 <= five_y < N:
            arr[five_x][five_y] += int(arr[x][y] * 0.05)
        else:
            out += int(arr[x][y] * 0.05)
        total += int(arr[x][y] * 0.05)
        for i in [-2, -1, 1, 2]:  # 2, 7%
            nx, ny = x, y + i
            if abs(i) == 2:
                first = 0.02
            else:
                first = 0.07
            if 0 <= nx < N and 0 <= ny < N:
                arr[nx][ny] += int(arr[x][y] * first)
            else:
                out += int(arr[x][y] * first)
            total += int(arr[x][y] * first)
        for xx, yy in [[1, -1], [1, 1]]:
            nx, ny = x + xx, y + yy
            if direction == 1:  #남쪽
                second = 0.1
            else:
                second = 0.01
            if 0 <= nx < N and 0 <= ny < N:
                arr[nx][ny] += int(arr[x][y] * second)
            else:
                out += int(arr[x][y] * second)
            total += int(arr[x][y] * second)
        for xx, yy in [[-1, -1], [-1, 1]]:
            nx, ny = x + xx, y + yy
            if direction == 1:
                third = 0.01
            else:
                third = 0.1
            if 0 <= nx < N and 0 <= ny < N:
                arr[nx][ny] += int(arr[x][y] * third)
            else:
                out += int(arr[x][y] * third)
            total += int(arr[x][y] * third)

    arr[x][y] -= total
    if 0 <= last_x < N and 0 <= last_y < N:
        arr[last_x][last_y] += arr[x][y]
    else:
        out += arr[x][y]
    arr[x][y] = 0
    return out


ans = 0
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
di = [[0, -1], [1, 0], [0, 1], [-1, 0]] # 서 남 동 북
a, b = N // 2, N // 2
n = 1
d = 0
cnt = 1
ans = 0
while a != 0 or b != 0:
    na, nb = a + di[d][0], b + di[d][1]
    if arr[na][nb]:
        amt = sand(na, nb, d)
        ans += amt
    if cnt >= n:
        if d in [1, 3]:
            n += 1
        d = d + 1 if d < 3 else 0
        cnt = 1
    else:
        cnt += 1
    a, b = na, nb

print(ans)
