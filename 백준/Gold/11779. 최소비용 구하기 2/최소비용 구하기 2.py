# 11779
# dijkstra로 접근
import heapq

def dijkstra(depart, arrival):
    heap = []
    heapq.heappush(heap, (0, depart, depart))
    while heap:
        time, city, connected = heapq.heappop(heap)
        if not visited[city]:
            previous[city] = connected
            visited[city] = 1
            dist[city] = time
            for new_c, new_t in arr[city]:
                if not visited[new_c]:
                    heapq.heappush(heap, (dist[city] + new_t, new_c, city))

n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    arr[s].append([e, c])
depart, arrival = map(int, input().split())

inf = 10**8
visited = [0] * (n+1)
previous = [-1] * (n+1)
dist = [inf] * (n+1)
dijkstra(depart, arrival)
idx = arrival
ans = [idx]
while idx != depart:
    idx = previous[idx]
    ans.append(idx)
ans.reverse()
print(dist[arrival])
print(len(ans))
print(*ans)
