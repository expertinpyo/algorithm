"""
연습 문제1.
"""

# 병합 정렬
def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    sorted_list = []
    l = r = 0

    while len(sorted_list) != len(left) + len(right):
        if left[l] <= right[r]:
            sorted_list.append(left[l])
            l += 1
        else:
            sorted_list(right[r])
            r += 1

        if r == len(right):
            sorted_list += left(l:)

def partition(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    left = partition(nums[:mid])
    right = partition(nums[mid:])
    return merge(left, right)


numbers = [0, 55, 22, 33, 2, 1, 10, 26, 42]
print(numbers)               # 정렬 전
print(partition(numbers))    # 정렬 후


# 퀵 정렬
def quick_sort():
    pass

def partition():
    pass

quick_nums = [0, 55, 22, 33, 2, 1, 10, 26, 42]