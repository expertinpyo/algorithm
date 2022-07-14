# 피자를 1번 위치에서만 넣고 뺄 수 있음
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())        # 화덕의 크기 n, 피자 개수 m
    arr = list(map(int, input().split()))
    pizza = []
    for i in range(n):
        pizza.append([arr.pop(0), i])
        num = i
    while num < m:
        p, pn = pizza.pop(0)
        p = p // 2
        if not p:
            if arr:
                num += 1
                pizza.append([arr.pop(0), num])
            else: break
        else:
            pizza.append([p, pn])

    while len(pizza) != 1:
        p, pn = pizza.pop(0)
        p = p//2
        if not p:
            continue
        else:
            pizza.append([p, pn])

    maxs = 0
    index = 0
    for i in pizza:
        if i[0] > maxs:
            maxs = i[0]
            index = i[1]

    print(f"#{tc} {index+1}")