# 연결하면 통신 가능
# 모든 다른 노드와의 통신이 가능해지도록 할 때의 최소비용
# S부터 각 A까지의 거리 계산 후 prim or kruskal 사용하면 될 듯
from collections import deque
import sys
sys.stdin = open('input.txt')

def bfs(a, b):
    queue = deque()
    queue.append([a, b])
    while queue:
        x, y = queue.popleft()
        for d in di:
            nx, ny = x + d[1], y + d[0]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != '#' and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)


def kruskal():
    global ans
    edge_cnt = 0
    for i in range(len(edges)):
        if edge_cnt == nums:
            return
        xx = edges[i][0]
        yy = edges[i][1]
        if find_set(xx) != find_set(yy):
            union(xx, yy)
            edge_cnt += 1
            ans += edges[i][2]



di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
no = '#_'
T = int(input())
for tc in range(1, T+1):
    m, n = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    spots = [0]
    nums = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] not in no:
                spots.append([i, j])
                nums += 1
    edges = []
    for s in range(1, len(spots)):
        visited = [[0]*m for _ in range(n)]
        bfs(spots[s][0], spots[s][1])
        for sp in range(1, len(spots)):
            if sp != s:
                edges.append([s, sp, visited[spots[sp][0]][spots[sp][1]]])

    edges.sort(key=lambda x:x[2])
    p = list(range(nums+1))
    ans = 0
    kruskal()
    print(ans)