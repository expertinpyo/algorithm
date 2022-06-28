import sys
sys.stdin  = open('input.txt')

def p(x, y, a):
    global minimum                      # 전역 변수
    if a > minimum:                     # a값이 최솟값 보다 크면 return
        return
    if x == n-1 and y == n-1:           # 마지막점에 도달했을때
        if a < minimum:                 # a값이 최솟값이라면 minimum 갱신
            minimum = a
    if x + 1 < n:                       # 아래로 이동이 가능한 경우
        p(x+1, y, a + arr[x+1][y])
    if y + 1 < n:                       # 오른쪽으로 이동이 가능한 경우
        p(x, y+1, a + arr[x][y+1])

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    minimum = 1000000               # 최솟값
    p(0, 0, arr[0][0])
    print(f"#{tc} {minimum}")