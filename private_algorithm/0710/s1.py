# 14719
# 빗물이 고인다
# 고인다는 것은 높이가 작거나 같을 때

# 풀이 1
# 투 포인터
#
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

# 풀이 2
# stack
stack = [arr[0]]

for i in range(1, W):
    if arr[i] <= stack[-1]:
        stack.append()