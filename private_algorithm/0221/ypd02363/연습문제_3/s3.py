"""
3. dfs - 인접 리스트
"""

def dfs(v):
    visited[v] = 1  # 방문 체크
    print(visited)
    for w in g[v]:  # 정점 v의 인접 정점 w 중에서
        if not visited[w]:  # 아직 방문하지 않은 정점이 있다면
            dfs(w)


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, e = map(int, input().split())
# 간선 정보 초기화
temp = list(map(int, input().split()))
# Graph 초기화
g = [[] for _ in range(V+1)]
for i in range(1, len(temp), 2):
    g[temp[i-1]].append(temp[i])
    g[temp[i]].append(temp[i-1])

# 방문 표시 초기화
visited = [0]*(V+1)
# dfs 탐색 시작
dfs(1)