# Kruskal
import sys
sys.stdin = open('input.txt')

def make_set(x):
    p[x] = x

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)

def kruskal():
    global ans
    edge_cnt = idx = 0

    while edge_cnt != v:    # 마지막 인덱스가 아니라면
        x = edges[idx][0]   # start
        y = edges[idx][1]   # end

        if find_set(x) != find_set(y):   # 같은 그룹이 아니라면
            union(x, y)
            edge_cnt += 1           # 연결되었으므로 더해주기
            ans += edges[idx][2]    # 가중치 더하기
        idx += 1


T = int(input())
for tc in range(1, T+1):
    ans = 0
    v, e = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(e)]
    p = [0] * (v+1)
    edges = sorted(edges, key=lambda x: x[2])

    for i in range(v+1):
        make_set(i)
    kruskal()
    print(f"#{tc} {ans}")
