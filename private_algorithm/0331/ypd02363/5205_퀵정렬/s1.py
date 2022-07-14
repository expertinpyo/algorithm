import sys
sys.stdin = open('input.txt')

def quicksort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end)
        quicksort(a, begin, p-1)
        quicksort(a, p+1, end)

def partition(a, begin, end):
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

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    quicksort(arr, 0, n-1)
    print(f'#{tc} {arr[n//2]}')