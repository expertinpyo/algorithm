T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        print(f"Case #{tc}: {1}")
    else:
        max_n = max(arr)
        min_n = min(arr)
        if min_n >= n:
            print(f"Case #{tc}: {n}")
        else:
            v = [0] * (max_n + 1)
            for i in range(n):
                v[arr[i]] += 1
            cnt = 0
            for i in range(4, max_n+1):
                if i >= cnt + v[i]:
                    cnt += v[i]
                else:
                    cnt = i
            print(f"Case #{tc}: {cnt}")