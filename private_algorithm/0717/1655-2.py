import sys
import heapq as hq
input = sys.stdin.readline
n = int(input())
leftheap = []
rightheap = []
for i in range(n):
    num = int(input())
    if len(leftheap) == len(rightheap):
        hq.heappush(leftheap, -num)
    else:
        hq.heappush(rightheap, num)

    if rightheap and -leftheap[0] > rightheap[0]:
        left, right = hq.heappop(leftheap), hq.heappop(rightheap)
        hq.heappush(leftheap, -right)
        hq.heappush(rightheap, -left)
    print(-leftheap[0])