import sys
sys.stdin = open("input.txt")
# 문제의 핵심은 다음과 같다.
# W, B, R은 각각 최소 한 줄 이상씩 있어야 한다.
# W - B - R 순서로 구성되어야 한다.
# 최종적으로 최솟값이 나와야 한다.
# 각 색깔별 경우의 수를 따질 수 있다.
# 예시 01 11 12 등
# 0001 0012 1112
def russia(arr, n, m):
    cnt_w = 0                       # w로 바꿔야 하는 개수
    ans = n * m                     # 초기 최솟값 = 전체 개수
    for i in range(n-2):            # n-2 까지
        cnt_w += m - arr[i].count("W")
        cnt_b = 0                   # b로 바꿔야 하는 개수
        for j in range(i+1, n-1):   # w가 i 번 째 까지이므로 i + 1 부터
            cnt_b += m - arr[j].count("B")
            cnt_r = 0               # r로 바꿔야 하는 개수
            for k in range(j+1, n): # b가 j 번째 까지 이므로 j + 1 부터
                cnt_r += m - arr[k].count("R")
            cnt = cnt_w + cnt_b + cnt_r
            if cnt < ans:
                ans = cnt
    return ans
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    print(f"#{tc} {russia(arr, n, m)}")