# 찾은 규칙
# 한 줄에 무조건 하나의 퀸이 있어야 함
# 현 코드의 문제점 : return 후 기존의 리스트들이 변해야하나 변하지 않음

import sys
sys.stdin = open('input.txt')

def chess(x, y, st, pl, mi, vi):
    global ans
    if x == n-1:
        ans += 1
        print(vi)
        return

    idx = 0
    while pl.count(n-1):
        if pl[idx] == n-1:
            pl.pop(idx)
        else:
            idx += 1

    for p in range(len(pl)):
        pl[p] += 1

    idx = 0
    while mi.count(0):
        if mi[idx] == 0:
            mi.pop(idx)
        else:
            idx += 1

    for m in range(len(mi)):
        mi[m] -= 1

    for j in range(n):
        if j not in st and j not in pl and j not in mi and j != y + 1 and j != y - 1:
            if y == 0:
                chess(x+1, j, st + [j], pl + [y+1], mi, vi + [x+1, j])
            elif y == n-1:
                chess(x+1, j, st + [j], pl, mi + [y-1], vi + [x+1, j])
            elif 0 < y < n-1:
                chess(x + 1, j, st + [j], pl + [y+1], mi + [y-1], vi + [x+1, j])


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    ans = 0
    for i in range(n):
        straight = [i]
        minus = []
        plus = []
        visible = [0, i]
        chess(0, i, straight, plus, minus, visible)
    print(f"#{tc} {ans}")

