import sys

sys.stdin = open('input.txt')


def post_order(node):
    if node:
        a = post_order(table[node][0]) if post_order(table[node][0]) else 0
        b = post_order(table[node][1]) if post_order(table[node][1]) else 0
        if table[node][3]:
            return table[node][3]
        else:
            table[node][3] = a + b
            return table[node][3]


T = int(input())
for tc in range(1, T + 1):
    n, m, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    table = [[0] * 4 for _ in range(n + 1)]
    for i in range(1, n + 1):
        table[i][2] = i // 2  # 부모 노드
        if i * 2 + 1 <= n:
            table[i][0] = i * 2
            table[i][1] = i * 2 + 1
        elif i * 2 == n:
            table[i][0] = i * 2

    for i in range(m):  # 리프노드 table에 배치
        table[arr[i][0]][3] = arr[i][1]

    ans = 0
    post_order(1)
    print(table)
    print(f"#{tc} {table[l][3]}")
