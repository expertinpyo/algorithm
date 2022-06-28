# 최소 배터리 사용량
import sys
import copy
sys.stdin = open('input.txt')

def p(N, k):
    if N == k:
        asd = copy.copy(s)
        nums.append(asd)
    else:
        for i in range(k):
            if not visited[i]:
                visited[i] = 1
                s[N] = number[i]
                p(N+1, k)
                visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    number = list(range(1, n))
    visited = [0] * (n-1)
    s = [0] * (n-1)
    nums = []
    p(0, n-1)
    mins = 1000000
    for num in nums:
        a = arr[0][num[0]]
        for i in range(n-2):
            if a > mins:
                break
            a += arr[num[i]][num[i+1]]
        a += arr[num[-1]][0]
        if mins > a:
            mins = a

    print(f"#{tc} {mins}")