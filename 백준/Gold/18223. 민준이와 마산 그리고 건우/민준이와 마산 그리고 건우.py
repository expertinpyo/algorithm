import heapq
from copy import deepcopy

def dijkstra(i):
    heap = []
    heapq.heappush(heap, (0, i, [i]))

    while heap:
        w, n, route = heapq.heappop(heap)

        if dist[n] < w:
            continue

        if n == V and P in route:
            return True

        for new_n, new_w in arr[n]:
            if dist[new_n] >= new_w + w:
                new_route = deepcopy(route)
                new_route.append(new_n)
                dist[new_n] = new_w + w
                heapq.heappush(heap, (new_w + w, new_n, new_route))

    return False

V, E, P = map(int, input().split())

arr = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

inf = float("inf")
dist = [inf] * (V+1)

string = dijkstra(1)
if string:
    print("SAVE HIM")
else:
    print("GOOD BYE")
