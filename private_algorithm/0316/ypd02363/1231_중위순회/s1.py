import sys
sys.stdin = open('input.txt')

def in_order(node):
    if node:
        in_order(table[node][0])
        print(arr[node-1][1], end='')
        in_order(table[node][1])

for tc in range(1, 11):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    table = [[0, 0, 0] for _ in range(N+1)]
    for i in range(N):
        parent = int(arr[i][0])
        if len(arr[i]) == 4:
            ch1 = int(arr[i][2])
            ch2 = int(arr[i][3])
            table[parent][0] = ch1
            table[parent][1] = ch2
            table[ch1][2] = parent
            table[ch2][2] = parent
        elif len(arr[i]) == 3:
            ch = int(arr[i][2])
            table[parent][0] = ch
            table[ch][2] = parent
    print(table)
    print(f"#{tc}", end=' ')
    in_order(1)
    print()