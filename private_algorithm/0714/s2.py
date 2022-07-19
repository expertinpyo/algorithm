# 오큰수
# 17289

N = int(input())
arr = list(map(int, input().split()))

max_n = 0
max_idx = 0
for i in range(N):
    for j in range(i, N):
        if i < max_idx:
            if arr[i] < max_n:
                print(max_n, end=' ')
                break
            else:

    else:
        print(-1, end=' ')