import sys
sys.stdin = open('input.txt')

def pascal(n):
    arr = [0] * n
    for i in range(1, n+1):
        arr[i-1] = [1] * i
        if i >= 3:
            for j in range(1, len(arr[i-1]) - 1):
                arr[i-1][j] = arr[i-2][j-1] + arr[i-2][j]           
        print(*arr[i-1])

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    print('#{}'.format(tc))
    pascal(n)