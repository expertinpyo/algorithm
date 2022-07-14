# 다익스트라로 문제 해결해보자
# 노드 번호랑 연결 되어있는 것 일뿐
# 가중치는 문제 없다
import heapq

def dijkstra():
    heap = []
    heapq.heappush(heap, (0, n))

    while heap:
        weight, number = heapq.heappop(heap)
        if number == k:
            print(weight)
            return
        if not visited[number]:
            visited[number] = 1
            dist[number] = weight
            for new_number, new_w in arr[number]:
                if not visited[new_number]:
                    heapq.heappush(heap, (dist[number] + new_w, new_number))


n, k = map(int, input().split())
mn = 10 ** 6
arr = [[] for _ in range(mn+1)]

for i in range(mn+1):
    a, b, c = i + 1, i - 1, i*2
    ar = [a, b, c]
    for r in ar:
        if r != i and r <= mn:
            if r != c:
                arr[i].append((r, 1))
            else:
                arr[i].append((r, 0))

inf = float('inf')
dist = [inf] * (mn+1)
visited = [0] * (mn+1)
dijkstra()