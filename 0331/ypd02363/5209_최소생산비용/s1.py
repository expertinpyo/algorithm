# 최소 생산 비용
# 행은 제품
# 열은 공장
import sys
sys.stdin = open('input.txt')

def find(ans, num):                 # ans 더해지는 값 / num 행 번호
    global mins                     # mins 최솟값
    if ans >= mins:                  # 가지치기, 재귀 실행 중 ans가 최솟값이 아니라면 return
        return

    if num == n:                    # 모든 행 다 봤으면
        mins = min(ans, mins)       # mins 갱신 후 return
        return

    for i in range(n):              # 각 행의 열별로
        if i not in visited:        # i가 visited에 없다면
            a = arr[num][i]         # 그 때의 값
            visited.append(i)       # visited에 추가
            find(ans+a, num+1)      # 재귀 실행
            visited.pop()           # pop


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    mins = 10000000             # 최솟값
    visited = []                # 방문했는지 여부
    find(ans, 0)                # 재귀함수 실행

    print(f"#{tc} {mins}")