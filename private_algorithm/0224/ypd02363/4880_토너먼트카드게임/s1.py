import sys
sys.stdin = open('input.txt')
# 각각 1명이 되면 양쪽의 카드를 비교
# 1 가위 2 바위 3 보
# 같은 카드일 시 번호가 작은쪽이 승자

def ranking(arr):
    if len(arr) == 2:
        if arr[0][1] == 1 and arr[1][1] == 2:
            return arr[1]
        elif arr[0][1] == 2 and arr[1][1] == 1:
            return arr[0]
        elif arr[0][1] == 1 and arr[1][1] == 3:
            return arr[0]
        elif arr[0][1] == 3 and arr[1][1] == 1:
            return arr[1]
        elif arr[0][1] == 2 and arr[1][1] == 3:
            return arr[1]
        elif arr[0][1] == 3 and arr[1][1] == 2:
            return arr[0]
        elif arr[0][1] == arr[1][1]:
            if arr[0][0] > arr[1][0]:
                return arr[1]
            else: return arr[0]
    if len(arr) == 1:
        return arr[0]

    pivot = (arr[0][0] + arr[-1][0]) // 2
    left = []
    right = []
    for i in range(len(arr)):
        if arr[i][0] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    a = ranking(left)
    b = ranking(right)
    c = ranking([a,b])
    return c

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    n_list = list(map(int, input().split()))
    arr = [[0, 0] for _ in range(n)]
    for i in range(n):
        arr[i][0] = i+1
        arr[i][1] = n_list[i]
    ans = ranking(arr)
    print(f"#{tc} {ans[0]}")