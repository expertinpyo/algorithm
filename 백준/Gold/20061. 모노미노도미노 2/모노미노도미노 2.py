# # 꽉 참 vs 연한 칸에 블록이 있는 경우 => 가득 찬 경우가 없을 때 까지 점수를 획득 먼저 => 그 이후 연한 칸에 블록이 있는 경우 처리
#
N = int(input())
blue = [[0] * 6 for _ in  range(4)]
green = [[0] * 4 for _ in  range(6)]
ans = 0
for _ in range(N):
    t, x, y = map(int, input().split())
    blues = False
    greens = False
    if t == 1:
        for i in range(5):
            if not blue[x][i] and blue[x][i+1] and not blues:
                blue[x][i] = 1
                blues = True
            if not green[i][y] and green[i+1][y] and not greens:
                green[i][y] = 1
                greens = True
            if blues and greens:
                break
        if not blues:
            blue[x][5] = 1
        if not greens:
            green[5][y] = 1

    else:
        if t == 2:
            if blue[x].count(1):
                left_idx = blue[x].index(1)
                blue[x][left_idx-1] = blue[x][left_idx-2] = 1
            else:
                blue[x][5] = blue[x][4] = 1

            for i in range(5):
                if not greens and (green[i+1][y] or green[i+1][y+1]):
                    green[i][y+1] = green[i][y] = 1
                    greens = True
                    break
            if not greens:
                green[5][y] = green[5][y+1] = 1
        else:
            for i in range(5):
                if not blues and (blue[x][i+1] or blue[x+1][i+1]):
                    blues = True
                    blue[x][i] = blue[x+1][i] = 1
                    break
            if not blues:
                blue[x][5] = blue[x+1][5] = 1

            for i in range(2, 6, 1):
                if green[i][y]:
                    green[i-1][y] = green[i-2][y] = 1
                    greens = True
                    break

            if not greens:
                green[5][y] = green[4][y] = 1

    # 디 돌았고, 확인 진행
    # 파랑색 점수 확인
    blue_check = []
    for i in range(5, 1, -1):
        cnt = 0
        for j in range(4):
            if blue[j][i]:
                cnt += 1
            if cnt == 4:
                # 1점 추가
                ans += 1
                # 한 칸씩 당기기 진행
                # 우선 해당 점 0으로 초기화
                for j in range(4):
                    blue[j][i] = 0
                blue_check.append(i)
    if len(blue_check):
        if len(blue_check) == 1:
            # 한 점만 이동했을 때
            for i in range(blue_check[0]-1, -1, -1):
                for j in range(4):
                    blue[j][i+1] = blue[j][i]
                    if not i:
                        blue[j][i] = 0
        else:
            # 두 점일 때
            blue_check.sort()
            for i in range(blue_check[0]-1, -1, -1):
                for j in range(4):
                    blue[j][i+2] = blue[j][i]
                if i <= 1:
                    blue[j][i] = 0


    # 초록색 점수 확인
    green_check = []
    for i in range(5, 1, -1):
        if green[i].count(1) == 4:
            ans += 1
            # 한 칸씩 당기기 진행
            # 1. 모든 점 0으로 초기화 진행
            for j in range(4):
                green[i][j] = 0
            green_check.append(i)
            # 2. 모든 점 한칸씩 아래로 이동 후 마지막 0으로 초기화
    if len(green_check):
        if len(green_check) == 1:
            # 한 점만 이동했을 때
            for i in range(green_check[0]-1, -1, -1):
                for j in range(4):
                    green[i+1][j] = green[i][j]
                    if not i:
                        green[i][j] = 0
        else:
            # 두 점일 때
            green_check.sort()
            for i in range(green_check[0]-1, -1, -1):
                for j in range(4):
                    green[i+2][j] = green[i][j]
                if i <= 1:
                    green[i][j] = 0


    # 중립 지역에 값 있는지 확인
    b_zero = b_one = 0
    for i in range(4):
        b_zero += 1 if blue[i][0] else 0
        b_one += 1 if blue[i][1] else 0
    if b_zero:
        # 두 값이 있을 떄
        for i in [5, 4]:
            for j in range(4):
                blue[j][i] = 0

        for i in range(3, -1, -1):
            for j in range(4):
                blue[j][i+2] = blue[j][i]
        for i in range(2):
            for j in range(4):
                blue[j][i] = 0

    elif b_one:
        # 한 값만 있을 때
        for j in range(4):
            blue[j][5] = 0
        for i in range(4, -1, -1):
            for j in range(4):
                blue[j][i+1] = blue[j][i]

    g_zero = green[0].count(1)
    g_one = green[1].count(1)

    if g_zero:
        for i in [5, 4]:
            for j in range(4):
                green[i][j] = 0
        for i in range(3, -1, -1):
            for j in range(4):
                green[i+2][j] = green[i][j]
        for i in range(2):
            for j in range(4):
                green[i][j] = 0
    elif g_one:
        for j in range(4):
            green[5][j] = 0
        for i in range(4, -1, -1):
            for j in range(4):
                green[i+1][j] = green[i][j]


total = 0
for i in range(6):
    for j in range(4):
        total += 1 if blue[j][i] else 0
        total += 1 if green[i][j] else 0

print(ans)
print(total)