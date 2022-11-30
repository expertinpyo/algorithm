import heapq
import sys
input = sys.stdin.readline

def dijkstra(i):
    heap = []
    heapq.heappush(heap, (0, i))
    dist = [inf] * (N+1)
    while heap:
        w, n = heapq.heappop(heap)
        if dist[n] < w:
            continue
        dist[n] = w
        for new_n, new_w in arr[n]:
            if dist[new_n] > new_w + w:
                dist[new_n] = new_w + w
                heapq.heappush(heap, (new_w + w, new_n))

    return dist

T = int(input())
for aaaaa in range(T):
    N, M = map(int, input().split())
    arr = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        arr[a].append((b, c))
        arr[b].append((a, c))
    K = int(input())
    friends = list(map(int, input().split()))
    inf = 10 ** 9
    answer = [inf] * (N + 1)
    for i in range(1, N+1):
        dist = dijkstra(i)
        answer[i] = sum(dist[f] for f in friends)
    print(answer.index(min(answer)))