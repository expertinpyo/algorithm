import sys
sys.stdin = open("input.txt")

def binary_search(page, num):
    start = 1
    end = page
    i = 0
    while start <= end:
        mid = int((start + end) / 2)
        i += 1
        if mid == num:
            return i
        elif mid > num:
            end = mid
        else:
            start = mid #문제조건 잘 확인해볼것,
    return 0

T = int(input())
for tc in range(1, T+1):
    page, pa, pb = map(int, input().split())
    a = binary_search(page, pa)
    b = binary_search(page, pb)

    if a < b:
        print(f"#{tc} A")
    elif b < a:
        print(f"#{tc} B")
    else:
        print(f"#{tc} 0")