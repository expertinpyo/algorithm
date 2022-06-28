"""
연습 문제1.
"""

# 병합 정렬
def merge(left, right):
    result = []
    while len(left) or len(right):
        if len(left) and len(right):
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    return result


def partition(li):
    if len(li) == 1:
        return li
    middle = len(li) // 2
    left = li[:middle]
    right = li[middle:]
    left = partition(left)
    right = partition(right)
    return merge(left, right)

numbers = [0, 55, 22, 33, 2, 1, 10, 26, 42]
print(numbers)               # 정렬 전
print(partition(numbers))    # 정렬 후


# 퀵 정렬
def quicksort(a, begin, end):
    if begin < end:
        p = partition2(a, begin, end)
        quicksort(a, begin, p-1)
        quicksort(a, p+1, end)

def partition2(a, begin, end):
    pivot = (begin + end) // 2
    l = begin
    r = end
    while l < r:
        while l < r and a[l] < a[pivot]:
            l += 1
        while l < r and a[r] >= a[pivot]:
            r -= 1
        if l < r:
            if l == pivot:
                pivot = r
            a[l], a[r] = a[r], a[l]
    a[pivot], a[r] = a[r], a[pivot]
    return r


quick_nums = [0, 55, 22, 33, 2, 1, 10, 26, 42]
quicksort(quick_nums, 0, len(quick_nums)-1)
print(quick_nums)