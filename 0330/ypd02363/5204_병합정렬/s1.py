import sys
sys.stdin = open('input.txt')

def merge(left, right):
    result = []

    l = r = 0
    while len(result) < len(left) + len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1

        else:
            result.append(right[r])
            r += 1

        if l == len(left):
            result += right[r:]
            break

        if r == len(right):
            result += left[l:]
            break

    return result


def partition(li):
    global ans
    if len(li) == 1:
        return li
    middle = len(li) // 2
    left = partition(li[:middle])
    right = partition(li[middle:])
    if left[-1] > right[-1]:
        ans += 1
    return merge(left, right)


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    print(f"#{tc} {partition(arr)[n//2]} {ans}")
