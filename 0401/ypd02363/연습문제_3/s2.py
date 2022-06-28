# kruskal 구현하기

import sys
sys.stdin = open('input.txt')

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)

def kruskal():
    global ans
    edge_cnt = 0
    for i in range(e):
        if edge_cnt == v:
            return
        x, y = edges[i][0], edges[i][1]
        if find_set(x) != find_set(y):
            union(x, y)
            edge_cnt += 1
            ans += edges[i][2]



v, e = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(e)]
edges.sort(key=lambda x:x[2])
ans = 0
p = list(range(v+1))
kruskal()
print(p)