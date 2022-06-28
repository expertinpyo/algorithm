"""
연습 문제2. 이진 탐색
 - 이진 탐색을 반복문과 재귀 함수를 활용하여 구현하시오.
 - 찾고자 하는 값(target)이 있다면 해당 값의 인덱스를 없다면 -1을 반환하시오.
"""

#1. iteration
def binary_search_iteration(key, l, r):
    while l <= r:
        mid = (l + r) // 2
        if nums1[mid] == key:
            return mid
        elif nums1[mid] > key:
            r = mid-1
        else:
            l = mid + 1

    return -1
nums1 = [6, 2, 3, 4, 5, 30, 1, 85, 10, 15, 40]
target1 = 2       # 있는 경우 -> 해당 요소의 인덱스 반환
# target = 90    # 없는 경우 -> -1
nums1.sort()
print(binary_search_iteration(target1, 0, len(nums1)-1))
print(binary_search_iteration(123, 0, len(nums1)-1))

#2. recursion
def binary_search_recursion(k, l, r):
    global mid
    if l <= r:
        mid = (l+r) // 2
        if nums2[mid] == k:
            return
        elif nums2[mid] > k:
            binary_search_recursion(k, l, mid-1)
        else:
            binary_search_recursion(k, mid+1, r)

    else:
        mid = -1
        return

nums2 = [6, 2, 3, 4, 5, 30, 1, 85, 10, 15, 40]
target2 = 2       # 있는 경우 -> 해당 요소의 인덱스 반환
# target = 90    # 없는 경우 -> -1
nums2.sort()
binary_search_recursion(123, 0, len(nums2)-1)
print(mid)