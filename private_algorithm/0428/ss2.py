# 그냥 왕창 머리채 잡고 꽉 끌어오는 느낌으로 될 것 같음

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
                if arr[i][j]:
                    a = i
                    for k in range(1, i+1):
                        if arr[i-k][j] == arr[a][j]:
                            arr[i-k][j] *= 2
                            arr[a][j] = 0
                        else:
                            if not arr[i-k][j]:
                                arr[i-k][j] = arr[a][j]
                                arr[a][j] = 0
                                a = i-k
                            else:
                                break
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
                if arr[i][j]:
                    a = i
                    for k in range(1, n):
                        if arr[i - k][j] == arr[a][j]:
                            arr[i - k][j] *= 2
                            arr[a][j] = 0
                        else:
                            if not arr[i - k][j]:
                                arr[i - k][j] = arr[a][j]
                                arr[a][j] = 0
                                a = i - k
                            else:
                                break
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