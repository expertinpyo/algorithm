import sys
sys.stdin = open('input2.txt')

T = int(input())
for tc in range(1, T+1):
    n, m , k = map(int, input().split()) # 셀의 개수 n / 격리 시간 m / 미생문 군집 개수 k
    arr = [list(map(int, input().split())) for _ in range(k)] # 세로, 가로, 미생물 수 , 이동 방향 수
    direction = {
        1:[0, -1],
        2:[0, 1],
        3:[-1, 0],
        4:[1, 0]
    }
    square = [[0]*n for _ in range(n)]
    for i in range(n):
        square[0][i] = square[i][0] = square[n-1][i] = square[i][n-1] = -1
    for i in range(k):
        square[arr[i][0]][arr[i][1]] = arr[i][2]        # 기본 값 배열
    while m:                # m시간만큼 확인
        dic = dict()
        for i in range(k):
            if arr[i][2]:
                x, y = arr[i][0], arr[i][1]
                nx, ny = x + direction[arr[i][3]][1], y + direction[arr[i][3]][0]
                if (nx, ny) in dic:
                    dic[(nx, ny)].append([x, y, i])
                else:
                    dic[(nx, ny)] = [[x, y, i]]
        for key in dic:
            # dic[key][0][2] : arr의 인덱스
            if len(dic[key]) == 1:  # 값이 하나일 때
                square[key[0]][key[1]] = arr[dic[key][0][2]][2]
                if square[arr[dic[key][0][2]][0]][arr[dic[key][0][2]][1]] == square[key[0]][key[1]]:
                    square[arr[dic[key][0][2]][0]][arr[dic[key][0][2]][1]] = 0
                if key[0] in [0, n-1] or key[1] in [0, n-1]:        # 방역 범위 내에 있다면
                    arr[dic[key][0][2]][2] //= 2                    # 값은 2배 감소하고
                    square[key[0]][key[1]] = arr[dic[key][0][2]][2]
                    if arr[dic[key][0][2]][3] % 2:                  # 방향은 변경된다.
                        arr[dic[key][0][2]][3] += 1
                    else:
                        arr[dic[key][0][2]][3] -= 1
                arr[dic[key][0][2]][0], arr[dic[key][0][2]][1] = key[0], key[1]

            else:       # 방문 점이 여러개일 때
                king = -100                 # 인덱스 컨트롤 할 예정
                for j in range(len(dic[key])):
                    square[key[0]][key[1]] += arr[dic[key][j][2]][2]
                    square[arr[dic[key][j][2]][0]][arr[dic[key][j][2]][1]] = 0
                    if arr[dic[key][j][2]][2] > king:
                        num = dic[key][j][2]
                        king = arr[dic[key][j][2]][2]
                for j in range(len(dic[key])):
                    if arr[dic[key][j][2]][2] != king:
                        arr[dic[key][j][2]][2] = 0
                arr[num][2] = square[key[0]][key[1]]
                arr[num][0], arr[num][1] = key[0], key[1]

        m-=1
    ans = 0
    for i in range(k):
        ans += arr[i][2]
    print(f'#{tc} {ans}')