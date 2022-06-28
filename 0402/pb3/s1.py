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
            for i in range(1, max_n+1):
                if not v[i]:
                    for j in range(i+1, max_n+1):
                        if v[j]:
                            v[j] -= 1
                            v[i] += 1
                            break
            nv = v[1::]
            if nv.count(0):
                ans = nv.index(0)
            else:
                ans = len(nv)
            print(f"Case #{tc}: {ans}")