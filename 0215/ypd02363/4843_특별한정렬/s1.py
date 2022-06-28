import sys
sys.stdin = open("input.txt")

def special_sort(arr, n):
    new_arr = [0] * n
    arr.sort()
    for i in range(n//2):
        new_arr[2*i] = arr[n-1-i]
        new_arr[2*i+1] = arr[i]
    return new_arr

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    new_arr = special_sort(arr, n)
    print(f"#{tc}", end=" ")
    for i in range(10):
        print(new_arr[i], end=" ")
    print()