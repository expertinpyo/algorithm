from itertools import combinations as cb
from collections import deque


def route(li):
    queue = deque()
    queue.append(li[0])
    cnt = 1
    while queue:
        x = queue.popleft()
        if not visited[x]:
            visited[x] = 1
        if cnt == len(li):
            return True
        for k in arr[x]:
            if not visited[k] and k in li:
                visited[k] = 1
                queue.append(k)
                cnt += 1
    return False


n = int(input())
p = [0] + list(map(int, input().split()))

arr = [[] for _ in range(n+1)]
for tc in range(1, n+1):
    small_list = list(map(int, input().split()))
    for i in range(1, small_list[0]+1):
        arr[tc].append(small_list[i])

# 배열 정리 끝
# 지역구 나누기
ans = 10**6
if n == 2:
    print(abs(p[1]-p[2]))
else:
    for i in range(1, n//2+1):
        combi = cb(list(range(1, n+1)), i) # i개 만큼 조합 생성
        for com in combi:
            first_check = list(com)          # 확인하고자 하는 번호
            second_check = list(set(tuple(range(1, n+1))) - set(com)) # 포함 안된 부분들
            visited = [0]*(n+1)
            sms = 0
            for f in first_check:
                sms += p[f]
            sms = abs(sms*2 - sum(p))
            if sms < ans:
                if route(first_check):
                    if route(second_check):
                        ans = sms

    if ans == 10**6:
        ans = -1
    print(ans)