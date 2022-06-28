import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    max_num, min_num = 0, 1000000

    for j in range(n-m+1):
        num = 0
        for k in range(m):
            num += arr[j+k]
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    print(f"#{i} {max_num - min_num}")
