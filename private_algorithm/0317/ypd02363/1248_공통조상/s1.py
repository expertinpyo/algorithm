import sys
sys.stdin = open('input.txt')

def find(x, list_c):
    if x:
        list_c.append(x)
        find(table[x][2], list_c)

def order(x):
    global ans
    if x:
        ans += 1
        order(table[x][0])
        order(table[x][1])

T = int(input())
for tc in range(1, T+1):
    v, e, a, b = map(int, input().split())
    arr = list(map(int, input().split()))
    table = [[0]*3 for _ in range(v+1)]
    for i in range(e):
        if not table[arr[i*2]][0]:
            table[arr[i*2]][0] = arr[i*2+1]
        else:
            table[arr[i*2]][1] = arr[i*2+1]
        table[arr[2*i+1]][2] = arr[i*2]
    list_a = []
    list_b = []
    find(a, list_a)
    find(b, list_b)
    for i in list_b:
        if i in list_a:
            num = i
            break
    ans = 0
    order(num)
    print(f"#{tc} {num} {ans}")