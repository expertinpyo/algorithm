import sys
sys.stdin = open('input.txt')

def bfs():
    minus = 1
    while True:
        if minus > 5:
            minus = 1
        q = arr.pop(0)
        a = q-minus
        if a <= 0:
            a = 0
            arr.append(a)
            break
        arr.append(a)
        minus += 1

for tc in range(1, 11):
    tcc = int(input())
    arr = list(map(int, input().split()))
    bfs()
    print(f"#{tc}", end=' ')
    print(*arr)