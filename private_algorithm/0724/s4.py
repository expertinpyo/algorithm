# # 17298
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
visited = [0] * N
max_n = 0
max_idx = -1
for i in range(N):
    if i >= max_idx:
        idx = -1
        max_n = 0
    if arr[i] > max_n:
        for j in range(i+1, N):
            if arr[j] > arr[i]:
                max_n = arr[j]
                idx = j
                print(arr[j], end=' ')
                break
        else:
            print(-1, end=' ')
    else:
        for j in range(i+1, idx):
            if arr[j] > arr[i]:
                idx = j
                max_n = arr[j]
                print(arr[j], end=' ')
                break
        else:
            print(arr[idx], end=' ')

