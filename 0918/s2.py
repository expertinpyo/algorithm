# 1806 부분합
# 부분합 중 그 합이 S이상 되는 것 중 가장 짧은 것의 길이
# S 이상
# 전략
# 1. 길이가 1일때 부터 전체 탐색
from sys import stdin
input = stdin.readline

N, S = map(int, input().split())
prefix = [0] * N
arr = list(map(int, input().split()))
prefix[0] = arr[0]
for i in range(1, N):
    prefix[i] = prefix[i-1] + arr[i]
ans = prefix.index(S) if S in prefix else 10 ** 6
trial = 1
left = 0
while trial <= N if ans == 10 ** 6 else trial < ans:
    if left + trial >= N:
        left = 0
        trial += 1
    right = left + trial
    if prefix[right] - prefix[left] < S:
        left += 1
    else:
        if right - left <= ans:
            ans = right - left
            print(ans)
            exit()
if ans < 10 ** 6:
    print(ans)
else:
    print(0)
