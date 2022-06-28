# 1238
# 오고 가는데 가장 많은 시간을 소요한 사람 찾기
# 이동은 최단 거리로 이동
# prim


import heapq
def prim():
    global ans
    heap = []
    heapq.heappush(heap, (0, x))

    while heap:
        time, student = heapq.heappop(heap)
        if not visited[student]:
            visited[student] = 1
            ans += time
            for s, w in arr[student]:
                if not visited[s]:
                    heapq.heappush(heap, (w, s))




n, m, x = map(int, input().split())
arr = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, weight = map(int, input().split())
    arr[start].append([end, weight])

ans = 0
visited = [0] * (n+1)
prim()
print(ans)