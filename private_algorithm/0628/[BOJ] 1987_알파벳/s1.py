# 0행 0열부터 시작
# 같은 알파벳이 적힌 칸 두번 지날 수 없음
# 최대 지날 수 있는 칸 개수 찾기
# 1 <= R C <= 20
# 시작점 고정
di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

stack_alpha = [arr[0][0]]
stack = [(0, 0)]
ans = 0
while True:
    x, y = stack.pop()
    for d in di:
        nx, ny = d[1] + x, d[0] + y
        if 0 <= nx < R and 0 <= ny < C:
            if arr[nx][ny] not in stack_alpha:
                stack_alpha.append(arr[nx][ny])
                stack.append((nx, ny))
            else:
                ans = max(ans, len(stack_alpha))
