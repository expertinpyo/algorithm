# kruskal
import sys
sys.stdin = open('input.txt')


def distance(x, y, nx, ny):
    return ((x-nx)**2 + (y-ny)**2) ** 0.5

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)

def kruskal():
    global ans
    edge_cnt = 0
    for i in range(len(group)):
        if edge_cnt == n-1:
            return
        x = group[i][0]
        y = group[i][1]

        if find_set(x) != find_set(y):
            union(x, y)
            ans += group[i][2] ** 2
            edge_cnt += 1

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    x_axis = list(map(int, input().split()))
    y_axis = list(map(int, input().split()))
    E = float(input())
    group = []

    for i in range(n):
        for j in range(n):
            if j != i:
                group.append([i, j, distance(x_axis[i], y_axis[i], x_axis[j], y_axis[j])])
    group = sorted(group, key=lambda x: x[2])
    ans = 0
    p = list(range(n))
    kruskal()
    print(f"#{tc} {round(ans * E)}")
