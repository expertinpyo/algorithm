import sys
import heapq
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    heap = []
    for i in range(n):
        heapq.heappush(heap, arr[i])
    print(heap)
    ans = 0
    while n > 1:
        ans += heap[n//2 - 1]
        n //= 2
    print(f'#{tc} {ans}')