def prim():
    global ans
    heap = []
    heapq.heappush(heap, (0,0))
    while heap:
        w, v = heapq.heappop(heap)
        if not visited[v]:
            ans += w
            visited[v] = 1
            for w, weight in G[v]:
                if not visited[w]:
                    heapq.heappush(heap, (weight, w))
    return ans


import sys
import heapq
sys.stdin = open('input.txt')
V, E = map(int, input().split())                        # V개의 정점 -> 0부터 시작하기 때문에 개수는 +1이 된다는 점 유의
G = [[] for _ in range(V+1)]                            # 인접 리스트
ans = 0                                                 # 누적 할 가중치
visited = [0] * (V+1)                                   # 정점의 선택 여부 체크
for i in range(E):
    start, end, W = map(int, input().split())           # 간선만큼 돌면서 두 정점과 가중치를 받고 인접 리스트 구현
    G[start].append([end, W])                           # 무방향 그래프 -> (정점, 가중치) 형태로 추가
    G[end].append([start, W])
print(prim())