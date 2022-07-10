H, W = map(int, input().split())
arr = list(map(int,input().split()))

left, right = 0, W-1
ans = 0
left_max, right_max = arr[left], arr[right]
while left < right:
    left_max = max(arr[left], left_max)
    right_max = max(arr[right], right_max)
    if left_max <= right_max:
        ans += left_max - arr[left]
        left += 1
    else:
        ans += right_max - arr[right]
        right -= 1
print(ans)