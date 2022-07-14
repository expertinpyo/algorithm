import sys
sys.stdin = open('input.txt')

def dfs(x ,y):
    if len(num) == 7:                           # 길이가 7이라면,
        sen = ''                                # num에 있는 값들 하나로 뭉쳐서 ans에 넣기
        for k in num:
            sen += k
        ans.append(sen)
        return                                  # dfs 종료
    for di in range(4):                         # 네 방향 탐색
        nx = x + delta[di][1]                   # nx, ny 정의
        ny = y + delta[di][0]
        if 0 <= nx < 4 and 0 <= ny < 4:         # 범위 내 값들이라면
            num.append(arr[nx][ny])             # num에 추가
            dfs(nx, ny)                         # 재귀 dfs 진행
            num.pop()                           # 끝난 후 에는 pop해서 리스트 끝 요소 하나씩 빼주기

delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]          # delta
T = int(input())
for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)] # 4x4 배열 input
    ans = []                                        # 빈 리스트
    for i in range(4):
        for j in range(4):
            num = [arr[i][j]]                       # 모든 점에 대해 dfs 진행
            dfs(i, j)
    print(f"#{tc} {len(set(ans))}")                 # set으로 중복값 제거
