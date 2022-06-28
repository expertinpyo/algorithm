import sys
sys.stdin = open('input.txt')

def chess(x, y, st, pl, mi, vi):
    global ans
    if x == n-1:            # 퀸을 넣을 수 있을 때
        ans += 1            # ans += 1
        # print(vi)
        return

    for j in range(n):
        # st : 직선(세로) 통제 / j-(x+1) : 우 하향 방향 통제 / j + (x+1) : 좌 하향 방향 통제
        # 가로 방향은 어차피 한 행에 하나의 퀸만 가능하므로, x+1로 재귀하는 것으로 퉁칠 수 있다.
        if j not in st and (j - (x+1)) not in pl and (j - (x+1) != y - x) and (j + (x+1)) not in mi and (j + (x+1) != y + x):
            # st에는 늘 새로운 세로 방향 요소를 통제해줘야 하므로 j값을 넣어준다
            # y == 0인 경우, 좌 하향 방향은 고려대상 아님, 따라서, 그냥 mi 넣어주기
            if y == 0:
                chess(x+1, j, st + [j], pl + [y-x], mi, vi + [x+1, j])
            # y == n-1인 경우, 우 하향 방향은 고려대상 아님, 따라서, 그냥 pl 넣어주기
            elif y == n-1:
                chess(x+1, j, st + [j], pl, mi + [y+x], vi + [x+1, j])
            # 두 경우에 해당되지 않는 경우, pl, mi에 해당되는 값들 각자 추가해주기
            elif 0 < y < n-1:
                chess(x + 1, j, st + [j], pl + [y-x], mi + [y+x], vi + [x+1, j])


T = int(input())
for tc in range(1, T+1):
    n = int(input())                # n의 수
    ans = 0                         # 결과값
    for i in range(n):
        straight = [i]              # 직선을 제한하는 수를 담는 리스트
        minus = []                  # 음의 대각 방향을 제한하는 리스트
        plus = []                   # 양의 대각 방향을 제한하는 리스트
        visible = [0, i]            # 확인차 생성한 리스트
        chess(0, i, straight, plus, minus, visible)     # (0, i)에서 탐색 시작
    print(f"#{tc} {ans}")

