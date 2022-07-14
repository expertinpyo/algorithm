import sys
sys.stdin = open("input.txt")

def selection_sort(nums):
    l = len(nums)
    for i in range(l-1):
        idx = i
        for j in range(i+1, l):
            if nums[idx] > nums[j]:
                idx = j
        nums[i], nums[idx] = nums[idx], nums[i]
    return nums

numbers = list(map(int, input().split()))
print(numbers)
print(selection_sort(numbers))