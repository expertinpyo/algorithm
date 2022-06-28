import sys
sys.stdin = open("input.txt")

def sudoku(arr):
    n = 0
    for ar in arr:
        for i in range(9):
            a = set(ar[i])
            if len(a) == 9:
                n += 1
    if n == 27:
        return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    arr_h = [list(map(int, input().split())) for _ in range(9)]
    arr_v = list(zip(*arr_h))
    arr_square = []
    for k in range(9):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                arr_square1 = arr_h[i][j], arr_h[i][j+1], arr_h[i][j+2], arr_h[i+1][j], arr_h[i+1][j+1], arr_h[i+1][j+2], arr_h[i+2][j], arr_h[i+2][j+1], arr_h[i+2][j+2]
                arr_square.append(arr_square1)
    print(f"#{tc} {sudoku([arr_h, arr_v, arr_square])}")
