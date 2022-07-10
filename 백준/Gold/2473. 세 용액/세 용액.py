n = int(input())
arr = sorted(list(map(int, input().split())))

cnt = float('inf')
for i in range(n-2):
    b = i + 1
    c = n-1
    while b != c:
        value = arr[i] + arr[b] + arr[c]
        if abs(value) < cnt:
            cnt = abs(value)
            ans = sorted([arr[i], arr[b], arr[c]])
            if not value:
                print(*ans)
                exit()
        if value > 0:
            c -= 1
        elif value < 0:
            b += 1
print(*ans)