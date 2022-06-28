"""
2. dfs - 인접 행렬 - 재귀
"""

def dfs(v):
    if not visited[v]:
        visited[v] = 1
    else:
        return
    print(visited)
    for i in range(V+1):
        if g[v][i] and not visited[i]:
            dfs(i)

import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, e = map(int, input().split())
# 간선 정보 초기화
temp = list(map(int, input().split()))
# Graph 초기화
g = [[0 for _ in range(V+1)] for _ in range(V+1)]
for i in range(e):
    g[temp[2 * i]][temp[2 * i + 1]] = 1
    g[temp[2 * i + 1]][temp[2 * i]] = 1
# 방문 표시 초기화
visited = [0]*(V+1)
# dfs 탐색 시작
dfs(1)