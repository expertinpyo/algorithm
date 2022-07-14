# n개의 집
# 각 집에는 한 명씩 살고 있음
# n개의 집을 정점으로 볼 때
# 도로는 다른 어떤 집으로 이동 가능한 단방향 간선
# 도로는 모든 집들 간에 이동이 가능하도록 구성되어 있음
# 인수의 집, X번으로 모인다.
# 가장 오래 걸리는 집을 찾기
# dijkstra의 냄새가 나는 문제

import heapq
import sys
sys.stdin = open('input.txt')

def dijkstra(visited, p, num):
    heap = []
    heapq.heappush(heap, (0, num))

    while heap:
        weight, node = heapq.heappop(heap)
        if not visited[node]:
            visited[node] = 1
            p[node] = weight
            for i in range(1, n+1):
                if not visited[i]:
                    heapq.heappush(heap, (p[node]+group[node][i], i))


T = int(input())
for tc in range(1, T+1):
    n, m, xx = map(int, input().split())
    group = [[10**6]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        x, y, c = map(int, input().split())
        group[x][y] = c
    visited = [0]*(n+1)
    p = [10**6] * (n+1)
    dijkstra(visited, p, xx)

    ans = 0
    for i in range(1, n+1):
        if i != xx:
            visited2 = [0] * (n+1)
            pp = [10**6] * (n+1)
            dijkstra(visited2, pp, i)
            ans2 = p[i] + pp[xx]
            ans = max(ans, ans2)
    print(f'#{tc} {ans}')