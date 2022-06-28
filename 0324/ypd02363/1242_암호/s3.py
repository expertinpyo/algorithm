# 16진수로 이뤄져 있음
# 이 배열을 2진수로 변환하여 안에 포함되어있는 암호코드 정보 확인해야함
import sys
from math import gcd
sys.stdin = open('input.txt')

def ascii_to_hex(c):
    if c <= '9':
        return ord(c) - ord('0')
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
    n, m = map(int, input().split())                # 크기
    arr = [list(input()) for _ in range(n)]         # input 값
    ans_2 = []                                      # 빈 리스트
    a_killer = []                                   # 빈 리스트, 이미 확인한 코드는 확인하지 않을 예정
    for a in arr:
        if a.count('0') < m and a not in a_killer:  # 요소가 0이 아니고, 아직 검토하지 않은 코드라면
            t = []
            pos = -1
            for k in a:
                hex_to_binary(ascii_to_hex(k))      # 이진수로 변환 후 t에 담기
            for l in range(len(t)-1, -1, -1):       # 첫 번째 시작점 탐색
                if t[l]:
                    pos = l     # 첫 번째 시작점
                    break

            while True:
                ans = []        # 빈 리스트
                num = 7         # 초기 건너 뛰는 값
                while t[pos] and pos > num:   # t[pos]가 1이라면, 즉 코드가 있다면
                    convert = []    # 빈 리스트
                    cnt = 1         # 비율을 구하기 위한 변수
                    for i in range(pos, pos-num, -1):   # pos부터, pos-num+1까지
                        if len(convert) == 3:           # 코드 길이가 3인 경우
                            break                       # 바로 딕셔너리와 검토를 위해 break
                        if t[i] == t[i-1]:              # 숫자가 같으면 cnt + 1
                            cnt += 1
                        else:                           # 아니라면 convert에 추가 후 cnt 초기화
                            convert.append(cnt)
                            cnt = 1
                    if len(convert) != 3:               # convert가 3이 아니라면 num + 7 후 다시 진행
                        num += 7
                        continue

                    c = []                              # 빈 리스트
                    for asd in range(2, -1, -1):        # convert를 역순으로 c로 바꿔준다
                        c.append(convert[asd])
                    if not c.count(1):                  # c에 1이 없다면
                        while not c.count(1):           # 1이 나올 때 까지
                            g = gcd(c[0], c[1], c[2])   # 최대 공약수 구하기
                            for asd in range(3):
                                c[asd] //= g
                    ans.append(P[tuple(c)])             # ans에 추가해주기
                    pos -= num                          # pos - num (다음을 위해)
                if len(ans) == 8:                       # ans 길이가 8이라면, 즉 코드를 다 찾았다면
                    odd = 0                             # 계산 진행
                    for o in range(7, 0, -2):
                        odd += ans[o]
                    even = 0
                    for e in range(6, 1, -2):
                        even += ans[e]
                    if (odd * 3 + even + ans[0]) % 10 == 0: # 유효한 코드라면
                        if ans not in ans_2:                # 코드를 빈 리스트에 추가
                            ans_2.append(ans)               # a 추가
                            a_killer.append(a)

                check = t[:pos+1]
                if check.count(1):
                    for pp in range(pos, -1, -1):
                        if t[pp]:
                            t = check
                            pos = pp
                            break

                else:
                    break

    ans_num = 0
    for asdasd in ans_2:
        ans_num += sum(asdasd)
    print(f"#{tc} {ans_num} {ans_2}")
