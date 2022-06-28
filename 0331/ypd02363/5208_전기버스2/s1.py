# 정류장에는 교체용 충전지가 있는 교환기 있음
# 충전지마다 최대로 운행할 수 있는 정류장 수 정해짐
# 충전지가 방전되기 전에 교체해야 함
# 최소한의 교체 횟수로 목적지에 도착해야함
# 최소한의 교환횟수를 출력하는 프로그램

import sys
sys.stdin = open('input.txt')

def bus(num, capacity, cnt):        # num 현재위치 / capacity 배터리 용량 / cnt 충전횟수
    global mins, arrival
    if num + capacity >= n:
        mins = min(cnt, mins)
        return
    if cnt >= mins:
        return
    for i in range(num+1, num+capacity+1):
        bus(i, capacity+battery[i]-(i-num), cnt+1)
        if cnt >= mins - 1:
            return


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    n = arr[0]
    battery = [0] + arr[1:]
    mins = n
    bus(1, battery[1], 0)
    print(f"#{tc} {mins}")