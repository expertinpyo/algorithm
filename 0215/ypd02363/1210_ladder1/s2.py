import sys
sys.stdin = open("input2.txt")


T = int(input())
arr = [list(map(int, input().split())) for _ in range(100)]
di = [1, 0, 0]
dj = [0, 1, -1]  #위로 올라갈 일 없음, 아래, 오른쪽, 왼쪽
direction = 0

for i in range(100):
    ans = 0
    x = 0
    y = i
    if arr[0][i]:
        while True:
            # print(x, y, arr[x][y])
            if arr[x][y] == 2:
                ans = i
            if x == 99: break
            nx = x + di[direction]
            ny = y + dj[direction]
            if 0 <= nx < 100 and 0 <= ny < 100 and arr[nx][ny]:
                x, y = nx, ny
                if direction == 0:
                    if ny == 0:
                        if arr[nx][ny + 1]:
                            direction = 1
                    elif ny == 99:
                        if arr[nx][ny - 1]:
                            direction = 2
                    else:
                        if arr[nx][ny + 1] or arr[nx][ny - 1]:
                            if arr[nx][ny + 1]:
                                direction = 1

                            elif arr[nx][ny - 1]:
                                direction = 2

                elif direction == 1:
                    if ny == 99:
                        direction = 0
                    else:
                        if not arr[nx][ny + 1]:
                            direction = 0

                elif direction == 2:
                    if ny == 0:
                        direction = 0
                    else:
                        if not arr[nx][ny - 1]:
                            direction = 0

    else: continue
    print(f"#{i} {ans}")