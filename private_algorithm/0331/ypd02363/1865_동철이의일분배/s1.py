import sys
sys.stdin = open('input.txt')

def pos(num, p):
    global maxs                             # 최댓값 비교 변수
    if num >= 2:                            # 가지치기를 위해, p를 퍼센테이지로 변환
        p *= 0.01
    if num == n:                            # 모든 요소를 다 본 후 maxs값 갱신
        maxs = max(maxs, p)
        return
    if p <= maxs:                           # 가지치기, p가 max보다 작으면 return
        return
    for i in range(n):
        if i not in working and arr[num][i]:    # i가 일하고 있지 않고, 0이 아니라면
            working.append(i)                   # 리스트에 추가
            pos(num+1, p*arr[num][i])           # 재귀
            working.pop()                       # pop

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    maxs = 0
    working = []                            # 빈 리스트
    pos(0, 1)                               # 재귀함수
    print("#{} {:.6f}".format(tc, maxs))