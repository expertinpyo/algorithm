# 사용할 수 있는 연산 +1, -1, *2, -10
# 최소 몇 번의 연산이 필요한지
# 연산의 중간 결과도 항상 백만 이하이여야 함

import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(n):
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == m:
            return
        num = [x+1, x*2, x-1, x-10]
        for i in num:
            if 0 < i <= 10**6 and not visited[i]:
                visited[i] = visited[x]+1
                queue.append(i)




T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    visited = [0] * (10**6+1)
    bfs(n)
    print(f"#{tc} {visited[m]}")