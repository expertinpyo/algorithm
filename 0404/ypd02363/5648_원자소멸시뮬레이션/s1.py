# 방향이 바뀌진 않고, 1초에 1씩 움직임
# 0: 상 / 1: 하 / 2: 좌 / 3: 우
# 고려해야 하는 점
# 1. 마주보는 방향일 때 서로가 서로에게 향하는지를 알아야 함
# 2. 대각선 방향일 때 경우를 나눠서 계산하기
# 3. 해당 점에서 최솟 거리에 있는지를 확인하기
# 2번 6번 확인해보기
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dic = dict()
    dic_distance = dict()
    for ar in arr:
        x, y, di, am = ar[0], ar[1], ar[2], ar[3]                           # 첫번째 점
        for i in range(n):
            nar = arr[i]
            nx, ny, ndi, nam = nar[0], nar[1], nar[2], nar[3]   # 두번째 점
            if ar != nar and di != ndi:  # 서로 같지 않을 때
                if di // 2 == ndi // 2:     # 마주보는 방향일 때
                    if not di // 2 and x == nx:         # x좌표가 똑같다면 => 세로로 접근한다면
                        min_y = min(y, ny)              # 둘 중 작은 y값
                        ydi = di if min_y == y else ndi # 작은 값의 방향 찾기
                        if ydi == 0:                    # 작은 y값을 가진 점이 위로 향한다면(올바른 방향)
                            if (x, y) in dic:
                                dic[(x, y)] += [[nx, ny, abs(y - ny)/2, am]]
                            else:
                                dic[(x, y)] = [[nx, ny, abs(y - ny)/2, am]]
                    elif di // 2 and y == ny:       # y좌표가 똑같다면 => 가로로 접근한다면
                        min_x = min(x, nx)          # 둘 중 작은 x값
                        xdi = di if min_x == x else ndi # 작은 값의 방향 찾기
                        if xdi == 3:                    # 작은 x값을 가진 점이 왼쪽에 있다면(올바른 방향)
                            if (x, y) in dic:
                                dic[(x, y)] += [[nx, ny, abs(x - nx)/2, am]]
                            else:
                                dic[(x, y)] = [[nx, ny, abs(x - nx)/2, am]]

                else:   # 마주보는 방향이 아니라, 대각으로 위치할 때
                    if di == 0: # di가 위로 갈 때
                        if (ndi == 2 and y < ny and x < nx) or (ndi == 3 and y < ny and x > nx):
                            if abs(nx-x) != 0 and (abs(ny-y)/abs(nx-x)) == 1:
                                if (x, y) in dic:
                                    dic[(x, y)] += [[nx, ny, abs(y - ny), am]]
                                else:
                                    dic[(x, y)] = [[nx, ny, abs(y - ny), am]]
                    elif di == 1: # di가 아래로 갈 때
                        if (ndi == 2 and y > ny and x < nx) or (ndi == 3 and y > ny and x > nx):
                            if abs(nx-x) != 0 and (abs(ny-y)/abs(nx-x)) == 1:
                                if (x, y) in dic:
                                    dic[(x, y)] += [[nx, ny, abs(y - ny), am]]
                                else:
                                    dic[(x, y)] = [[nx, ny, abs(y - ny), am]]
                    elif di == 2:
                        if (ndi == 0 and y > ny and x > nx) or (ndi == 1 and y < ny and x > nx):
                            if abs(nx-x) != 0 and (abs(ny-y)/abs(nx-x)) == 1:
                                if (x, y) in dic:
                                    dic[(x, y)] += [[nx, ny, abs(y - ny), am]]
                                else:
                                    dic[(x, y)] = [[nx, ny, abs(y - ny), am]]

                    elif di == 3:
                        if (ndi == 0 and y > ny and x < nx) or (ndi == 1 and y < ny and x < nx):
                            if abs(nx-x) != 0 and (abs(ny-y)/abs(nx-x)) == 1:
                                if (x, y) in dic:
                                    dic[(x, y)] += [[nx, ny, abs(y - ny), am]]
                                else:
                                    dic[(x, y)] = [[nx, ny, abs(y - ny), am]]

    for key in dic:
        dic[key].sort(key=lambda x:x[2])    # distance별로 오름차순 정렬 완료
    total = 0

    visited = []
    for key in dic:
        if key not in visited:
            ans = 0
            original_distance = dic[key][0][2]  # 단순히 가장 작은 distance
            for val in dic[key]:                # key에 있는 value들 탐색
                new_key = tuple(val[:2])        # new_key
                if new_key not in visited:
                    new_distance = dic[new_key][0][2]
                    if val[2] == original_distance and new_distance == original_distance and new_key not in visited:
                        ans += dic[new_key][0][-1]
                        visited.append(new_key)
                    # 그냥 바껴버리는 경우가 있음
            if ans:
                ans += dic[key][0][-1]  # 자기 자신의 값 더하기
                visited.append(key)

            total += ans

    print(f"#{tc} {total}")
