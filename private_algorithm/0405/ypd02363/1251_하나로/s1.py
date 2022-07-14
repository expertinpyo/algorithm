# 모든 섬을 연결해야 한다
# 터널 당 환경 부담금이 있음
# 환경 부담금 : E(세율) * L(해저터널 길이)^2
# 환경 부담금을 최소로 하려면, 최단 거리가 되어야 함
# 하나에서 찾고 둘에서는 범위가 줄어들면 된다. visited를 다시 하나 더 만들어서 4 3 2 1이렇게 가면 되지 않을까 싶다

import heapq
import sys
from math import inf
sys.stdin = open('input.txt')


def distance(x, y, nx, ny):
    return ((x-nx)**2 + (y-ny)**2) ** 0.5

def dijkstra(num):
    heap = []
    heapq.heappush(heap, (0, num))
    while heap:
        weight, node = heapq.heappop(heap)
        if not visited[node]:
            visited[node] = 1
            p[node] = weight
            for i in range(len(group[node])):
                new_node, new_weight = group[node][i]
                if not visited[new_node]:
                    heapq.heappush(heap, (p[node] + new_weight, new_node))


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    x_axis = list(map(int, input().split()))
    y_axis = list(map(int, input().split()))
    E = float(input())
    # 각 섬의 길이를 다익스트라로 표기한 후 그 것을 가지고 돌리면 될 것 같다.
    group = [[inf] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if j != i:
                group[i][j] = distance(x_axis[i], y_axis[i], x_axis[j], y_axis[j])
    # visited = [0]*n
    # p = [10**6]*n
    # # for i in range(n):
    # dijkstra(0)
    # print(p)
    for k in range(n):
        group[k][k] = 0
        for i in range(n):
            for j in range(n):
                group[i][j] = min(group[i][j], group[i][k] + group[k][j])
    ans = 0
    visited = [0]*n
    for i in range(n):
        g_target = group[i]
        visited[i] = 1
        mins = 10 ** 6
        pos = False
        for j in range(n):
            if not visited[j] and j != i:
                if g_target[j] < mins:
                    idx = j
                    mins = g_target[j]
                    pos = True
        if pos:
            visited[idx] = 1
            ans += mins**2
    print(f"#{tc} {round(ans*E, 1)}")