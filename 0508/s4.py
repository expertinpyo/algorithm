# 1504
# 1번 정점에서 n번으로 이동하되 임의의 주 정점은 반드시 통과한다
import heapq

def dijkstra(x):
    heap = []
    heapq.heappush(heap, (0, x))

    while heap:
        weights, number = heapq.heappop(heap)
        if not visited[number]:
            visited[number] = 1
            dist[number] = weights
            for new_n, new_w in arr[number]:
                if not visited[new_n]:
                    heapq.heappush(heap, (dist[number] + new_w, new_n))

n, e = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(e):
    start, end, weight = map(int, input().split())
    arr[start].append([end, weight])
    arr[end].append([start, weight])
inf = 10**8
v1, v2 = map(int, input().split())
check_list = [1, v1, n]
d_list = []
ans = 0
for i in check_list:
    visited = [0] * (n+1)
    dist = [inf] * (n+1)
    dijkstra(i)
    d_list.append(dist)

if d_list[1][v2] == inf:
    ans = -1
elif d_list[0][v1] == d_list[2][v1] == inf:
    ans = -1
elif d_list[0][v2] == d_list[2][v2] == inf:
    ans = -1
elif d_list[2][v1] == d_list[2][v2] == inf:
    ans = -1


if not ans:
    ans = min(d_list[0][v1]+d_list[1][v2]+d_list[2][v2], d_list[0][v2]+d_list[1][v2]+d_list[1][n])
print(ans)
