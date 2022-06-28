import sys
sys.stdin = open('input.txt')

def bus(location, capacity, cnt):
    global mins
    if cnt >= mins:     # 충전횟수가 최솟값 보다 크다면, 가지치기
        return
    if location == n:   # location이 n이라면 (종착역 도착) mins 갱신
        mins = min(mins, cnt)
        return
    if capacity:        # capacity가 있다면 (이동할 수 있는 횟수가 있다면)
        bus(location+1, capacity-1, cnt)    # capacity -1, 이동거리 + 1, 충전횟수 변화 없음
    bus(location+1, battery[location]-1, cnt+1) # capacity가 0이라면, location+1, 충전해주기, 충전 횟수 + 1

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    n = arr[0]
    battery = [0] + arr[1:]   # 배터리가 있는 곳의 용량
    mins = n                  # 초기 변수 값
    bus(1, battery[1], 0)    # 현재 위치, 현재 배터리 용량, 충전 횟수
    print(f"#{tc} {mins}")