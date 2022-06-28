# 5000개의 버스 정류장
# N개의 버스 노선
# i 번째 버스 노선은 a 이상 b 이하인 정류장만 지남
# p 개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지!

import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    bus_stop = []
    for i in range(n):
        bus_stop.append(list(map(int, input().split())))
    p = int(input())
    bus_num = []
    for j in range(p):
        bus_num.append(int(input()))
    ans_list = []
    for i in range(p):
        c = bus_num[i]
        num = 0
        for j in range(n):
            a, b = bus_stop[j]
            new_list = list(range(a,b+1))
            if c in new_list:
                num += 1
        ans_list.append(num)
    print(f"#{tc}", *ans_list)