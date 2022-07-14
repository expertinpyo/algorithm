import sys
sys.stdin = open("input.txt")

#n*n 행렬 중 m*m 영역을 읽는다.
def fly_killer(arr, n, m):
    ans_list = []
    for k in range(n-m+1):
        for j in range(n - m + 1):
            total = 0
            for i in range(m):
                total += sum(arr[i+k][j:j+m:1])
                ans_list.append(total)
    return max(ans_list)

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(n)]
    print(f"#{tc} {fly_killer(arr, n, m)}")
