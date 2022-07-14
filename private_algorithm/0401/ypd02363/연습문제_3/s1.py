def make_set(x):
    """
    유일한 멤버 x를 포함하는 새로운 집합을 생성하는 연산
    """
    p[x] = x                     # 노드 x의 부모 저장

def find_set(x):
    """
    x를 포함하는 집합을 찾는 연산
    """
    if p[x] != x:                # x가 루트가 아닌 경우
        p[x] = find_set(p[x])    # 다시 루트 찾아서 재귀 호출
    return p[x]                  # x의 대표값 반환

def union(x, y):
    """
    x와 y를 포함하는 두 집합을 통합하는 연산
    """
    p[find_set(y)] = find_set(x) # y의 대표자를 x의 대표자로 변경


def kruskal():
    global ans
    edge_cnt = idx = 0

    while edge_cnt != V:
        x = edges[idx][0]
        y = edges[idx][1]

        if find_set(x) != find_set(y):
            union(x, y)
            edge_cnt += 1
            ans += edges[idx][2]
        idx += 1


import sys
sys.stdin = open('input.txt')
ans = 0
V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
p = [0] * (V+1)
edges = sorted(edges, key=lambda x: x[2])

for i in range(V+1):
    make_set(i)
kruskal()
print(ans)

