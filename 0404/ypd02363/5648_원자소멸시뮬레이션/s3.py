# 방향이 바뀌진 않고, 1초에 1씩 움직임
# 0: 상 / 1: 하 / 2: 좌 / 3: 우
# 고려해야 하는 점
# 1. 마주보는 방향일 때 서로가 서로에게 향하는지를 알아야 함
# 2. 대각선 방향일 때 경우를 나눠서 계산하기
# 3. 해당 점에서 최솟 거리에 있는지를 확인하기
# 2번 6번 확인해보기
# 최솟값을 구현하는 것을 다시 해야 할 듯

import sys
sys.stdin = open('input.txt')

delta = [(0, -1), (0, 1), (-1, 0), (1, 0)]
def calculation():
    global total

    while queue:
        x, y, di, am = queue.pop(0)
        if matrix[y][x] > am:
            total += matrix[y][x]
            matrix[y][x] = 0
            continue
        nx, ny = nx, ny = x + delta[di][0], y + delta[di][1]
        if 0 <= nx < 4002 and 0 <= ny < 4002:
            if not matrix[ny][nx]:
                queue.append((nx, ny, d, k))
            matrix[ny][nx] += k
        matrix[y][x] = 0

T = int(input())

matrix = [[0 for _ in range(4002)] for _ in range(4002)]
for tc in range(1, T+1):
    n = int(input())
    queue = []
    total = 0
    for i in range(n):
        x, y, di, am = map(int, input().split())
        if n > 1:
            queue.append((2*x + 2000, 2000 - 2*y, di, am))
    calculation()