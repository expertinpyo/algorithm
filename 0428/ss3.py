# 그냥 왕창 머리채 잡고 꽉 끌어오는 느낌으로 될 것 같음

from copy import deepcopy
from itertools import product as pd


def game(direction):
    if direction == 0:  # 위로 이동
        for j in range(n):
            visited = [0] * n
            for i in range(1, n, 1):
                a = i
                if arr[i][j]:
                    for k in range(i-1, -1, -1):
                        if arr[k][j] == arr[a][j]:
                            if not visited[k]:
                                arr[k][j] *= 2
                                arr[a][j] = 0
                                visited[k] = 1
                            else:
                                break
                        else:
                            if not arr[k][j]:
                                arr[k][j] = arr[a][j]
                                arr[a][j] = 0
                                a = k
                            else:
                                break
    elif direction == 2:  # 아래로 이동
        for j in range(n):
            visited = [0] * n
            for i in range(n-2, -1, -1):
                a = i   # 시작점
                if arr[i][j]:
                    for k in range(i+1, n, 1):
                        if arr[k][j] == arr[a][j]:
                            if not visited[k]:
                                arr[k][j] *= 2
                                arr[a][j] = 0
                                visited[k] = 1
                            else:
                                break
                        else:
                            if not arr[k][j]:
                                arr[k][j] = arr[a][j]
                                arr[a][j] = 0
                                a = k
                            else:
                                break

    elif direction == 1:  #오른쪽으로 이동
        for i in range(n):
            visited = [0] * n
            for j in range(n-2, -1, -1):
                a = j   # 시작점
                if arr[i][j]:
                    for k in range(j+1, n, 1):
                        if arr[i][k] == arr[i][a]:
                            if not visited[k]:
                                arr[i][k] *= 2
                                arr[i][a] = 0
                                visited[k] = 1
                            else:
                                break
                        else:
                            if not arr[i][k]:
                                arr[i][k] = arr[i][a]
                                arr[i][a] = 0
                                a = k
                            else:
                                break

    elif direction == 3:  #왼쪽으로 이동
        for i in range(n):
            visited = [0] * n
            for j in range(1, n, 1):
                a = j   # 시작점
                if arr[i][j]:
                    for k in range(j-1, -1, -1):
                        if arr[i][k] == arr[i][a]:
                            if not visited[k]:
                                arr[i][k] *= 2
                                arr[i][a] = 0
                                visited[k] = 1
                            else:
                                break
                        else:
                            if not arr[i][k]:
                                arr[i][k] = arr[i][a]
                                arr[i][a] = 0
                                a = k
                            else:
                                break





# 움직이는 방향 키보드 화살표 방향
n = int(input())
games = [list(map(int, input().split())) for _ in range(n)]
max_num = 0

pdlist = list(pd([0,1,2,3], repeat=5))

for pds in pdlist:
    arr = deepcopy(games)
    for p in pds:
        game(p)

    maxmax = 0
    for ar in arr:
        maxs = max(ar)
        maxmax = max(maxmax, maxs)

    max_num = max(max_num, maxmax)

print(max_num)