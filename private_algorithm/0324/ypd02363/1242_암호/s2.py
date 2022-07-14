# 16진수로 이뤄져 있음
# 이 배열을 2진수로 변환하여 안에 포함되어있는 암호코드 정보 확인해야함
import sys
from math import gcd
sys.stdin = open('input.txt')

def ascii_to_hex(c):
    # 9 이하
    if c <= '9':
        return ord(c) - ord('0')
    # 10 이상
    else:
        return ord(c) - ord('A') + 10

def hex_to_binary(x):
    global pos
    for i in range(4):
        t.append(asc[x][i])

asc = [[0, 0, 0, 0],  #0
       [0, 0, 0, 1],  #1
       [0, 0, 1, 0],  #2
       [0, 0, 1, 1],  #3
       [0, 1, 0, 0],  #4
       [0, 1, 0, 1],  #5
       [0, 1, 1, 0],  #6
       [0, 1, 1, 1],  #7
       [1, 0, 0, 0],  #8
       [1, 0, 0, 1],  #9
       [1, 0, 1, 0],  #A
       [1, 0, 1, 1],  #B
       [1, 1, 0, 0],  #C
       [1, 1, 0, 1],  #D
       [1, 1, 1, 0],  #E
       [1, 1, 1, 1]]  #F


P = {(2, 1, 1): 0,
     (2, 2, 1): 1,
     (1, 2, 2): 2,
     (4, 1, 1): 3,
     (1, 3, 2): 4,
     (2, 3, 1): 5,
     (1, 1, 4): 6,
     (3, 1, 2): 7,
     (2, 1, 3): 8,
     (1, 1, 2): 9}


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    ans_2 = []
    a_killer = []
    for a in arr:
        if a.count('0') < m and a not in a_killer:
            t = []
            pos = -1
            for k in a:
                hex_to_binary(ascii_to_hex(k))
            for l in range(len(t)-1, -1, -1):
                if t[l]:        # 2진법으로 나오는게 T
                    pos = l     # 첫번째 시작점
                    break

            while True:
                ans = []
                num = 7
                while t[pos]:
                    convert = []
                    cnt = 1
                    for i in range(pos, pos-num, -1):
                        if len(convert) == 3:
                            break
                        if t[i] == t[i-1]:
                            cnt += 1
                        else:
                            convert.append(cnt)
                            cnt = 1
                    if len(convert) != 3:
                        num += 7
                        continue

                    c = []
                    for asd in range(2, -1, -1):
                        c.append(convert[asd])
                    if not c.count(1):
                        while not c.count(1):
                            g = gcd(c[0], c[1], c[2])
                            for asd in range(3):
                                c[asd] //= g
                    ans.append(P[tuple(c)])
                    pos -= num
                    if len(ans) == 8:
                        odd = 0
                        for o in range(7, 0, -2):
                            odd += ans[o]
                        even = 0
                        for e in range(6, 1, -2):
                            even += ans[e]
                        if (odd * 3 + even + ans[0]) % 10 == 0:
                            if ans not in ans_2:
                                ans_2.append(ans)
                                a_killer.append(a)
                                ans = []
                check = t[:pos+1]
                if check.count(1):
                    for pp in range(pos, -1, -1):
                        if t[pp]:
                            pos = pp
                            break
                else:
                    break

    ans_num = 0
    for asdasd in ans_2:
        ans_num += sum(asdasd)
    print(f"#{tc} {ans_num}")
