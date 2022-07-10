n = int(input())
arr = sorted(map(int, input().split()))
num = float('inf')
left, right = 0, n-1
while left < right:
    value = arr[left] + arr[right]
    if abs(value) < num:
        num = abs(value)
        ans = [arr[left], arr[right]]
        if not value:
            break
    if value > 0:
        right -= 1
    else:
        left += 1
print(*ans)
