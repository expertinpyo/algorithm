# 16진수로 이뤄져 있음
# 이 배열을 2진수로 변환하여 안에 포함되어있는 암호코드 정보 확인해야함
import sys
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


code = [[[[[[[0 for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)]
code[0][0][0][1][1][0][1] = 0
code[0][0][1][1][0][0][1] = 1
code[0][0][1][0][0][1][1] = 2
code[0][1][1][1][1][0][1] = 3
code[0][1][0][0][0][1][1] = 4
code[0][1][1][0][0][0][1] = 5
code[0][1][0][1][1][1][1] = 6
code[0][1][1][1][0][1][1] = 7
code[0][1][1][0][1][1][1] = 8
code[0][0][0][1][0][1][1] = 9


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    for a in arr:
        t = []
        pos = -1
        for k in a:
            hex_to_binary(ascii_to_hex(k))
        for l in range(len(t)-1, -1, -1):
            if t[l]:
                pos = l
                break
        ans = []
        # print(f"#{tc} {len(t)}")
        while pos > 7:
            if not t[pos]:
                break
            sentence = code[t[pos-6]][t[pos-5]][t[pos-4]][t[pos-3]][t[pos-2]][t[pos-1]][t[pos]]
            ans.append(sentence)
            pos -= 7

        if ans:
            odd = 0
            for o in range(7, 0, -2):
                odd += ans[o]
            even = 0
            for e in range(6, 1, -2):
                even += ans[e]
            if (odd*3 + even + ans[0]) % 10 == 0:
                print(f"#{tc} {sum(ans)}")
                break
    else:
        print(f"#{tc} {0}")