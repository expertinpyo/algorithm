import heapq

def dijkstra(x):
    heap = []
    heapq.heappush(heap, (0, x))

    while heap:
        time, bus = heapq.heappop(heap)
        if not visited[bus]:
            visited[bus] = 1
            dist[bus] = time
            if bus == e:
                return
            for bus_number, weight in arr[bus]:
                if not visited[bus_number]:
                    heapq.heappush(heap, [dist[bus]+weight, bus_number])


n = int(input())
m = int(input())
arr = [[] for _ in range(m+1)]

for _ in range(m):
    start, end, distance = map(int, input().split())
    arr[start].append([end, distance])
s, e = map(int, input().split())


dist = [[10**6] for _ in range(n+1)]
visited = [0]*(n+1)
dijkstra(s)
print(dist[e])