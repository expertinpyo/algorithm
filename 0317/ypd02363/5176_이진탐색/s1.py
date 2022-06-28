import sys
sys.stdin = open('input.txt')

def order(x):
    global ans
    if x:
        order(table[x][0])
        table[x][2] = ans
        ans += 1
        order(table[x][1])

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    table = [[0]*3 for _ in range(n+1)]
    for i in range(1, n+1):
        if i*2 + 1 <= n:
            table[i][0], table[i][1] = 2 * i, 2 * i + 1
        elif i*2 == n:
            table[i][0] = 2*i
    ans = 1
    # print(table)
    order(1)
    # print(table)
    print(f"#{tc} {table[1][2]} {table[n//2][2]}")