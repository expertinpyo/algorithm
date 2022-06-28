import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    table = [[0]*3 for _ in range(n+1)]
    for i in range(1, n+1):
        if i*2 + 1 <= n:
            table[i][0] = i * 2
            table[i][1] = i * 2 + 1
        elif i*2 == n:
            table[i][0] = i*2
        table[i][2] = arr[i-1]
