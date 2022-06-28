

from copy import deepcopy

def game(direction, cnt):
    global max_num
    if cnt == 5:
        maxx = 0
        for ar in arr:
            maxx2 = max(ar)
            maxx = max(maxx, maxx2)
        max_num = max(maxx, max_num)
        return

    if direction == 0: # 위
        for i in range(1, n):
            for j in range(n):
                if arr[i-1][j]:
                    if arr[i-1][j] == arr[i][j]:
                        arr[i-1][j] *= 2
                        arr[i][j] = 0
                else:
                    arr[i-1][j] = arr[i][j]
                    arr[i][j] = 0
    # 200002
    elif direction == 1: # 오른쪽
        for i in range(n):
            for j in range(n-2, -1, -1):
                if arr[i][j+1]:
                    if arr[i][j] == arr[i][j+1]:
                        arr[i][j+1] *= 2
                        arr[i][j] = 0
                else:
                    arr[i][j+1] = arr[i][j]
                    arr[i][j] = 0

    if direction == 2:  # 아래
        for i in range(n-2, -1, -1):
            for j in range(n):
                if arr[i+1][j]:
                    if arr[i+1][j] == arr[i][j]:
                        arr[i+1][j] *= 2
                        arr[i][j] = 0
                else:
                    arr[i+1][j] = arr[i][j]
                    arr[i][j] = 0
    elif direction == 3: # 왼쪽
        for i in range(n):
            for j in range(1, n):
                if arr[i][j-1]:
                    if arr[i][j] == arr[i][j-1]:
                        arr[i][j-1] *= 2
                        arr[i][j] = 0
                else:
                    arr[i][j-1] = arr[i][j]
                    arr[i][j] = 0
    for i in range(4):
        game(i, cnt+1)


# 움직이는 방향 키보드 화살표 방향
n = int(input())
games = [list(map(int, input().split())) for _ in range(n)]
max_num = 0

for i in range(4):
    arr = deepcopy(games)
    game(i, 0)
print(max_num)