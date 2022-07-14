# MST PRIM

# PRIM
# 정점 중심
# 정점과 인접하는 정점 중에서 최소 비용의 간선이 존재하는 정점 선택
# 계속 가중치가 최소인 정점을 연결해가며 최종적으로 연결된 배열의 합
def prim():
    for _ in range(V):
        min_idx = -1
        min_value = 987654321

        # 1. 최솟값 찾기
        for i in range(V+1):
            if not visited[i] and key[i] < min_value:
                min_idx = i
                min_value = key[i]
        visited[min_idx] = 1

        #2. 해당 값으로부터 연결된 정점 가중치 갱신
        for i in range(V+1):
            if not visited[i] and G[min_idx][i] < key[i]:
                key[i] = G[min_idx][i]
    print(key)
    return sum(key)

import sys
sys.stdin = open('input.txt')
V, E = map(int, input().split())
G =[[987654321 for _ in range(V+1)] for _ in range(V+1)]
key = [987654321] * (V+1)
key[0] = 0
visited = [0] * (V+1)
for i in range(E):
    start, end, W = map(int, input().split())
    G[start][end] = W
    G[end][start] = W
print(prim())
