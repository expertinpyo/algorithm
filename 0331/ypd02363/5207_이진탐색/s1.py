# 양쪽 과정을 번갈아가며 선택한다
# m개의 정수에 대해 n에 들어있는지를 확인한다
# 시작 l 끝 r
# 중심원소 mid = (l+r) // 2
# 이진탐색 왼쪽 l ~ mid -1 / 오른쪽 mid + 1~ r
# 숫자가 a에 들어있으면서 탐색 과정에서 동시에 양쪽 구간을 번갈아 선택하게 되는 수


import sys
sys.stdin = open('input.txt')

def find(a, l, r, key):
    global ans, left, right, cnt
    if l > r:
        return
    else:
        cnt += 1
        mid = (l+r) // 2
        if key == a[mid]:
            ans += 1
        elif key < a[mid]:
            if cnt < 2 or (cnt >= 2 and right):
                left = True
                right = False
                return find(a, l, mid-1, key)
            else:
                return

        elif key > a[mid]:
            if cnt < 2 or (cnt >= 2 and left):
                right = True
                left = False
                return find(a, mid + 1, r, key)
            else:
                return

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr_n = sorted(list(map(int, input().split())))
    arr_m = list(map(int, input().split()))
    ans = 0
    for i in range(m):
        cnt = 0
        left = right = False
        what_we_need = arr_m[i]
        if what_we_need in arr_n:
            find(arr_n, 0, n-1, what_we_need)
    print(f"#{tc} {ans}")