# 1774
# kruskal이나 dijkstra로 접근해보자


N, M = map(int, input().split())
arr = []
already = []
for _ in range(N):
    arr.append(map(int, input().split()))
for _ in range(M):
    already.append(map(int, input().split()))

def find_set(x):
    while x != p[x]:
        p[x] = x

def union(x, y):
    pass

p = list(range(N))

