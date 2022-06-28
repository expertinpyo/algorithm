# Prim
import heapq
import sys
sys.stdin = open('input.txt')

def prim():
    global ans
    heap = []
    heapq.heappush(heap, (0, 0))    # 가중치, 정점
    while heap:
        w, node = heapq.heappop(heap)
        if not visited[node]:
            ans += w
            visited[node] = 1
            for x, y in group[node]:
                if not visited[x]:
                    heapq.heappush(heap, (y, x))
    return ans

T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())
    group = [[]*(v+1) for _ in range(v+1)]
    ans = 0
    visited = [0]*(v+1)
    for i in range(e):
        start, end, weight = map(int, input().split())
        group[start].append([end, weight])
        group[end].append([start, weight])
    print(f"#{tc} {prim()}")