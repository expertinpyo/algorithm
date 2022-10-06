import heapq

def dijkstra(i):
    heap = [(0, i, i)]

    visited = [0] * (n+1)
    while heap:
        weight, node, start_node = heapq.heappop(heap)
        if not visited[node]:
            if node == i:
                visited[node] = '-'
            else:
                visited[node] = start_node
            for new_node, new_weight in arr[node]:
                if not visited[new_node]:
                    if node == i:
                        heapq.heappush(heap, (new_weight + weight, new_node, new_node))
                    else:
                        heapq.heappush(heap, (new_weight + weight, new_node, start_node))
    visited = visited[1::]
    print(*visited)

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, amount = map(int,input().split())
    arr[start].append((end, amount))
    arr[end].append((start, amount))

for i in range(1, n+1):
    dijkstra(i)