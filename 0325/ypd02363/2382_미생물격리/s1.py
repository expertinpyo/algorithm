# n*n 배열 k개의 미생물
# m은 총 시간
# -1을 떠날 때 생각해야 함
# 처음에는 그냥 그 값을 바꿔주고 그 값이 겹치면 결정하는 것도 하나의 방법이 된다.
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m, k = map(int ,input().split())
    arr = [list(map(int, input().split())) for _ in range(k)]
    square = [[0]*n for _ in range(n)]
    direction = {
        1 : [0, -1],
        2 : [0, 1],
        3 : [-1, 0],
        4 : [1, 0],
    }
    for i in range(n):
        square[i][0] = square[0][i] = square[n-1][i] = square[i][n-1] = -1
        square[arr[i][0]][arr[i][1]] = arr[i][2]
    while m:
        visited = []
        for i in range(len(arr)):
            if arr[i][2]:
                x, y = arr[i][0], arr[i][1]
                nx = x + direction[arr[i][3]][1]
                ny = y + direction[arr[i][3]][0]
                visited.append((nx, ny))
        dic = {}
        for i in range(len(visited)):
            dic[visited[i]] = visited.count(visited[i])

        for i in range(len(arr)):
            if arr[i][2]:
                x, y = arr[i][0], arr[i][1]
                nx = x + direction[arr[i][3]][1]
                ny = y + direction[arr[i][3]][0]
                if 1 <= nx < n-1 and 1 <= ny < n-1:
                    if dic[(nx, ny)] == 1:
                        square[nx][ny] += arr[i][2]
                        arr[i][0], arr[i][1] = nx, ny
                    else:
                        square[nx][ny] += arr[i][2]
                        arr[i][0], arr[i][1] = nx, ny
                        for j in range(len(arr)):
                            if arr[j][0] == nx and arr[j][1] == ny and i != j:
                                if arr[i][2] > arr[j][2]:
                                    arr[j][2] = 0
                                    king = i
                                else:
                                    arr[i][2] = 0
                                    king = j
                                dic[(nx, ny)] -= 1
                                if not dic[(nx, ny)]:
                                    arr[king][2] = square[nx][ny]

                elif not nx*ny: # -1 지역에 있는 경우
                    arr[i][2] //= 2
                    square[nx][ny] = arr[i][2]
                    if arr[i][3] % 2:
                        arr[i][3] += 1
                    else:
                        arr[i][3] -= 1
                    arr[i][0], arr[i][1] = nx, ny
                if not x*y:
                    square[x][y] = -1
                else:
                    square[x][y] = 0
        m -= 1
    print(square)
    ans = 0
    for i in range(n):
        for j in range(n):
            if square[i][j] >= 1:
                ans += square[i][j]
    print(f"#{tc} {ans}")