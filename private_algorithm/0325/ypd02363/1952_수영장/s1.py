# 모든 경우를 탐색하는 것 : dfs
# dp : 가능한 경우를 미리 구해놓고 재귀 취하는 것

import sys
sys.stdin = open('input.txt')

def s(x, expenditure):                          # x : n월, expenditure : 가격
    global mins                                 # 최솟값 글로벌 변수 선언
    if x > 12:                                  # x > 12인 경우, 모든 월을 다 본 경우
        if mins > expenditure:                  # 최솟값이 expenditure보다 큰 경우
            mins = expenditure                  # 최솟값 초기화
            ans.append(expenditure)             # 정답에 추가
        return
    if not month[x]:                            # n월에 수강 계획이 없으면
        return s(x+1, expenditure)              # x+1월, expenditure
    else:                                       # 수강 계획이 있고, x <= 12 라면
        if expenditure > mins:                  # 가격이 최솟값보다 커지면 그냥 return
            return
        for i in range(4):
            if i == 0:                                  # 1일차 수강료 계산
                s(x+1, expenditure + price[i]*month[x])
            elif i == 1:                                # 한 달치 수강료 계산
                s(x + 1, expenditure + price[i])
            elif i == 2:                                # 세 달치 수강료 계산
                if x <= 10:                             # x가 10월까지 인 경우는 3달치 [(x+2)달까지] 할인 모두 받을 수 있음
                    s(x + 3, expenditure + price[i])    # 따라서, x+3으로 재귀함수 실행
                elif x == 11:                           # x가 11월인 경우, 11, 12월만 할인 받으므로
                    s(x + 2, expenditure + price[i])
                elif x == 12:                           # x가 12월인 경우, 당월 요금을 세 달치로 계산
                    s(x + 1, expenditure + price[i])
            elif i == 3:                         # 1년치 요금인 경우
                ans.append(price[i])             # 1년치 요금을 바로 추가 후 return
                return


T = int(input())
for tc in range(1, T+1):
    price = list(map(int, input().split()))     # 각 일차별 수강가격
    month = list(map(int, input().split()))     # n월달 별 수강일수
    month.insert(0, 0)      # 인덱스를 맞추기 위해 0 추가
    ans = []                # 정답
    mins = 1000000          # 최솟값
    s(1, 0)                 # 1월부터 시작, 0원
    print(f"#{tc} {min(ans)}")