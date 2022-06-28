# 10217
import heapq

def dijkstra_time():
    visited = [0] * (n + 1)
    dist = [inf] * (n + 1)
    heap = []
    heapq.heappush(heap, (0, 0, 1))
    while heap:
        time, cost, airport = heapq.heappop(heap)
        if not visited[airport]:
            visited[airport] = 1
            dist[airport] = (time, cost)
            for new_airport, new_cost, new_time in arr[airport]:
                if not visited[new_airport]:
                    heapq.heappush(heap, (new_time + time, new_cost + cost, new_airport))
    return dist


def dijkstra_cost():
    visited = [0] * (n + 1)
    dist = [inf] * (n + 1)
    heap = []
    heapq.heappush(heap, (0, 0, 1))
    while heap:
        cost, time, airport = heapq.heappop(heap)
        if not visited[airport]:
            visited[airport] = 1
            dist[airport] = (time, cost)
            for new_airport, new_cost, new_time in arr[airport]:
                if not visited[new_airport]:
                    heapq.heappush(heap, (new_cost + cost, new_time + time, new_airport))
    return dist


T = int(input())
for tc in range(T):
    n, m, k = map(int, input().split())
    arr = [[] for _ in range(n+1)]
    for _ in range(k):
        u, v, c, d = map(int, input().split())
        arr[u].append([v, c, d])
    inf = 10 ** 8
    dist_cost = dijkstra_cost()
    dist_time = dijkstra_time()

    possible = False
    ans = inf
    for dist in [dist_time, dist_cost]:
        if len(dist[n]) == 1:
            continue
        if dist[n][1] <= m and dist[n][0] < inf:
            possible = True
            ans = min(ans, dist[-1][0])
    if not possible:
        print('Poor KCM')
    else:
        print(ans)
