# 10282 해킹

# a - b, b가 감염되면 a도 감염된다.
# b가 a를 의존하지 않는다면 b는 안전해진다

# 총 몇대의 컴퓨터가 감염ㄴ되며 그에 걸리는 시간
import heapq

def dijkstra():
    heap = []
    cnt = 0
    last = 0
    heapq.heappush(heap, (0, c))
    while heap:
        weight, node = heapq.heappop(heap)
        if not visited[node]:
            cnt += 1
            visited[node] = 1
            last = weight
            for new_n, new_w in arr[node]:
                if not visited[new_n]:
                    heapq.heappush(heap, (weight+new_w, new_n))
    print(cnt, last)


T = int(input())
for tc in range(T):
    n, d, c = map(int, input().split())
    arr = [[] for _ in range(n+1)]
    inf = float('inf')
    for _ in range(d):
        a, b, s = map(int, input().split())
        arr[b].append((a, s))
    visited = [0] * (n+1)
    dijkstra()