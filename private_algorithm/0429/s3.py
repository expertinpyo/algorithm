# 스타트 택시
# 손님을 도착지로 데려다주면 연료 충전
# 연료 다 떨어지면 업무 종료
# 특정 위치 이동 시 최단 경로로 이동
# M명의 승객
# 한 번에 한 명의 승객만 가능
# 태울 승객을 고를 때에는 최단 거리가 가장 짧으 ㄴ 승객 고름
# 그런 승객이 많다면 번호가 가장 작은 승객
# 소모한 연료의 두배가 충전된다.
# 각 턴마다 승객 별 최단 거리 계산해야 함
# 약간 몬스터 문제랑 비슷한 듯
# N, M 초기 연료

# 동일 거리일 시 행번호 > 열번호로 진행한다

from collections import deque

def taxi(fuel):
    fuel = fuel
    empty = False
    cnt = 0
    dx, dy = driver[0][0] - 1, driver[0][1] - 1
    while cnt < m:
        if fuel < 0:    # 연료가 없다면
            fuel = -1
            break

        distance = 10**6
        for i in range(m):
            px, py = passangers[i][0]-1, passangers[i][1]-1
            if field[px][py] != -1:
                if field[px][py] < 1:
                    length = move(dx, dy, px, py)
                    if length >= 0:
                        if length < distance:
                            distance = length
                            idx = i
                        elif length == distance:
                            fx, fy = passangers[idx][0], passangers[1]
                            lx, ly = passangers[i][0], passangers[i][1]
                            if lx <= fx:
                                if lx < fx:
                                    distance = length
                                    idx = i
                                else:
                                    if ly < fy:
                                        distance = length
                                        idx = i

                    else:       # 길이가 - => 방문할 수 없다.
                        fuel = -1
                        break
        if fuel < 0:       # 길이가 -일 때
            break

        if fuel < distance:    # 손님을 태우기 전 손님한테까지의 거리
            fuel = -1
            break

        fuel -= distance        # 간 거리만큼 연료 소비

        destination = passangers[idx]   # 다음 이동을 위해
        field[destination[0]-1][destination[1]-1] = -1  # 방문처리(손님 픽업함)
        consume = move(destination[0]-1, destination[1]-1, destination[2]-1, destination[3]-1)

        if consume < 0:         # 손님이 원하는 목적지로 갈 수 없는 경우 break
            fuel = -1
            break

        if fuel < consume:      # 목적지까지 가는 데 연료가 부족할 경우
            fuel = -1
            break

        fuel += consume         #

        dx, dy = destination[2]-1, destination[3]-1
        cnt += 1

    print(fuel)

def move(dx, dy, px, py):
    queue = deque()
    queue.append([dx, dy])
    visited = [[0]*n for _ in range(n)]
    while queue:
        x, y = queue.popleft()
        if [x, y] == [px, py]:
            return visited[x][y]
        for d in di:
            nx, ny = d[1] + x, d[0] + y
            if 0 <= nx < n and 0 <= ny < n and field[nx][ny] < 1 and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])
    return -100

di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
n, m, fuel = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
driver = [list(map(int, input().split()))]  # 드라이버 위치
passangers = [list(map(int, input().split())) for _ in range(m)]  # 출발지 / 목적지
taxi(fuel)

