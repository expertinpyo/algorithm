# 17298
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
cnt = [0] * N
# 제일 큰 수를 담는 변수가 있고
# 내 값보다 작은 수를 만나면 갱신되는 변수가 있다
idx = N-1
max_n = c_n = arr[idx]
while idx >= 0:
    if arr[idx] >= max_n:
        cnt[idx] = -1
        max_n = arr[idx]
    else:
        if arr[idx] < c_n:  # current n보다 작을 때
            cnt[idx] = c_n
        elif arr[idx] < max_n:
            cnt[idx] = max_n
    if arr[idx-1] < arr[idx]:
        c_n = arr[idx]
    idx -= 1
print(*cnt)

