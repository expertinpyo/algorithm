import sys
sys.stdin = open('input.txt')

T = int(input())
arr = [list(map(int, input().split())) for _ in range(T)]

# 1. 행 우선
for i in range(len(arr)):
    for j in range(len(arr)):
        print(arr[i][j], end=' ')
print()

# 2. 열 우선
for i in range(len(arr)):
    for j in range(len(arr)):
        print(arr[j][i], end=' ')
print()

# 3. 지그재그
for i in range(len(arr)):
    for j in range(len(arr)):
        print(arr[i][j + (i % 2) * (len(arr)-1 - 2*j)], end=' ')
print()

# 4. 전치행렬
for i in range(len(arr)):
    for j in range(len(arr)):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print(arr)