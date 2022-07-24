from collections import deque

n = int(input())
queue = deque([])
mins, maxs = float('inf'), -float('inf')
idx = 0
for _ in range(n):
    num = int(input())
    if not len(queue):
        maxs = mins = num
        queue.append(num)
    elif num > maxs:
        maxs = num
        queue.append(num)
    elif num < mins:
        mins = num
        queue.appendleft(num)
    else:
        queue.append(num)
        queue = deque(sorted(list(queue)))
    idx = (len(queue)-1) // 2
    print(queue[idx])