# 11779
# 비용이라고 했지만, 거리일 것이다.
# kruskal 로 선 풀이
def find_set(x):
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)

def kruskal():
    idx = 0
    for i in range(m):
        if idx == n:
            return
        x, y, cost = arr[i]
        if p[x] != p[y]:
            union(x, y)
            idx += 1


n = int(input())
m = int(input())
arr = []
for _ in range(m):
    s, e, c = map(int, input().split())
    arr.append([s, e, c])
depart, arrival = map(int, input().split())
arr.sort(key = lambda x:x[2])
p = list(range(n+1))
kruskal()
print(p)
