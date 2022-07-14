# 두 명의 일꾼
# 꿀 채취 가능한 벌통 수 M
# 두 명의 일꾼이 선택한 벌통은 겹치면 안된다.
# 하나의 벌통에서 채취한 꿀은 하나의 용기에 담아야한다.
# 꿀의 최대 양 C

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m, c = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    new = []
    for i in range(n):
        for j in range(n-1):
            new.append([i, j, arr[i][j], arr[i][j+1], arr[i][j] + arr[i][j+1]])
    new.sort(key=lambda x:x[-1], reverse=True)
    coordinate = []
    case = []
    for i in range(len(new)):
        if new[i][-1] == c:
            if not coordinate:
                coordinate.append(new[i][0:2])
                case.append(new[i][2])
                case.append(new[i][3])
            else:
                for coor in coordinate:
                    if coor[0] == new[i][0] and abs(coor[1]-new[i][1]) == 1:
                        break
                else:
                    coordinate.append(new[i][0:2])
                    case.append(new[i][2])
                    case.append(new[i][3])
    ans = 0
    if case:
        for i in case:
            ans += i**2
    print(f'#{tc} {ans}')


