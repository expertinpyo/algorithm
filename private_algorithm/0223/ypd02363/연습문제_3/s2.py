def partition(arr, start, end):
    pivot = arr[0]
    s = start
    e = end
    while s < e:
        while s < e and arr[s] < arr[pivot]:
            s += 1
        while s < e and arr[e] >= arr[pivot]:
            e += 1
        if s < e:
            if s == pivot

def quick_sort(arr, start, end):
    if start < end:
        p = partition(arr, start, end)
        quick_sort(arr, start, p-1)
        quick_sort(arr, p+1, end)


# 고정 배열
import sys
sys.stdin = open('input.txt')
numbers = list(map(int, input().split()))
print(quick_sort(numbers, 0, len(numbers)-1))