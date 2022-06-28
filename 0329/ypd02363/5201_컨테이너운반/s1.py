# n개의 컨테이너를 m대의 트럭으로 운반
# 트럭당 한 개의 컨테이너 운반 가능 / 적재용량 초과 컨테이너 운반 불가
# 편도로 한번만 이동

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    truck.sort(reverse=True)
    ans = 0
    for t in truck:
        if not weight:      # 확인해보기. [0,0,0,0]
            break
        for i in range(n):
            if t >= max(weight):
                ans += max(weight)
                weight[weight.index(max(weight))] = 0
                break
            else:
                weight[weight.index(max(weight))] = 0

    print(f"#{tc} {ans}")
