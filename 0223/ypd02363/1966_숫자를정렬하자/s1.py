def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    left = []
    right = []
    for i in range(1, len(nums)):
        if nums[i] < pivot:
            left.append(nums[i])
        elif nums[i] >= pivot:
            right.append(nums[i])
    a = quick_sort(left)
    b = quick_sort(right)
    return [*a, pivot, *b]
# 가변 배열
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    ans = quick_sort(nums)
    print(f"#{tc}", end=" ")
    print(*ans)