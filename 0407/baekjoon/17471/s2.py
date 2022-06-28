# 1. bfs로 연결 되어있는지 확인
# 2. 연결 되어있으면 구간별로 확인
# 3. 연결 되어있지 않다면 몇개의 구역인지 확인
# 4. 구역이 3개 이상인 경우 -1 출력
# 5. 구역이 2개인 경우 그냥 거기서 최솟값 구해버리기

import sys
from collections import deque
input = sys.stdin.readline



def bfs(x):
    queue = deque([x])
    cnt = 1
    while queue:
        x = queue.popleft()
        if graph[x]:
            for i in range(1, n+1):
                if graph[x][i] and not visited[i]:
                    queue.append(i)
                    visited[x] = 1
                    gr[x][i] = cnt
        cnt += 1



n = int(input())
population = [0] + list(map(int, input().split()))
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    arrs = list(map(int, input().split()))
    for j in range(1, len(arrs)):
        graph[i][arrs[j]] = 1
        graph[arrs[j]][i] = 1

visited = [0]*(n+1)
gr = [[0]*(n+1) for _ in range(n+1)]
bfs(1)
print(gr)