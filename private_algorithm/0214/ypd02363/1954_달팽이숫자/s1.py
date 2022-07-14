import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    box_size = int(input())
    direction = 0
    arr = [[0]*box_size for _ in range(box_size)]
    x = y = 0 # 초기 위치
    di = [0, 1, 0, -1] # 델타 방향
    dj = [1, 0, -1, 0] # 델타 방향

    for i in range(1, box_size**2 + 1):
        arr[x][y] = i # arr 값 정의
        nx = x + di[direction] # 새로운 x 좌표 = 기존 좌표 + 방향
        ny = y + dj[direction] # 새로운 y 좌표 = 기존 좌표 + 방향

        if 0 <= nx < box_size and 0 <= ny < box_size and not arr[nx][ny]: # 새로운 좌표가 박스 사이즈 안에 있고, 그 값이 0일 때
            x, y = nx, ny # x, y = 새로운 좌표
        else: # 벽을 만나거나, 다음 값이 있을 때
            direction = (direction + 1) % 4 # 네 방향이므로
            x += di[direction] # 새로운 x 좌표에 방향 변경
            y += dj[direction] # 새로운 y 좌표에 방향 변경
    print(arr)