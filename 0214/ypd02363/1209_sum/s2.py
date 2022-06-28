
T = int(input())
arr = [list(map(int, input().split())) for i in range(100)]
row_sum = 0
column_sum = 0
for i in range(100):
    row, column, diagonal_r, diagonal_l = 0, 0, 0, 0
    for j in range(100):
        row += arr[i][j]
        column+= arr[j][i]
    if row > row_sum:
        row_sum = row
    if column > column_sum:
        column_sum = column
    diagonal_r += arr[i][i]
    diagonal_l += arr[i][99-i]
print(f"{T} {max(row_sum, column_sum, diagonal_r, diagonal_l)}")