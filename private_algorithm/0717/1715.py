# 우선순위 큐
# 중복적으로 더해지는 것이므로 작은 숫자를 계속해서 더하면 된다.
# 선 정렬 후
# 누적합 구하기
# 그 후 누적합의 합
import heapq

n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))
if n == 1:
    print(0)
else:
    ans = 0
    while heap:
        x, y = heapq.heappop(heap), heapq.heappop(heap)
        ans += (x+y)
        heapq.heappush(heap, x+y)
        if len(heap) == 1:
            break
    print(ans)

