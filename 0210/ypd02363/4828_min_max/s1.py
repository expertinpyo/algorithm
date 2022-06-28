import sys
sys.stdin = open('input.txt')

T = int(input())
for i in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    min, max = arr[0], arr[0]
    for j in range(N):
        if arr[j] < min:
            min = arr[j]
        if arr[j] > max:
            max = arr[j]
    print(f"#{i} {max - min}")