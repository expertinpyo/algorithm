# 1238
# kruskal


def kruskal():
    for i in range(m):
        x, y = arr[i][0], arr[i][1]
        if find_set(x) != find_set(y):
            union(x, y)
            ans_list[x] = arr[i][2]



def find_set(x):
    while x != p[x]:
        p[x] = x
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)

n, m, x = map(int, input().split())
arr = []

for _ in range(m):
    start, end, weight = map(int, input().split())
    arr.append([start, end, weight])

arr.sort(key=lambda x:x[2])
p = list(range(n+1))
ans = 0
ans_list = [0]*(n+1)
kruskal()
print(ans_list)