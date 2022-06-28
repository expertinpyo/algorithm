import sys
sys.stdin  = open('input.txt')

def subtree(n):
    global ans
    if table[n][0]:
        ans += 1
        subtree(table[n][0])
    if table[n][1]:
        ans += 1
        subtree(table[n][1])


T = int(input())
for tc in range(1, T+1):
    e, n = map(int, input().split())
    arr = list(map(int, input().split()))
    table = [[0, 0, 0] for _ in range(e+2)]
    for i in range(e):
        parent = arr[2*i]
        child = arr[2*i+1]
        if not table[parent][0]:
            table[parent][0] = child
        else:
            table[parent][1] = child
        table[child][2] = parent
    ans = 1
    subtree(n)
    print(f"#{tc} {ans}")