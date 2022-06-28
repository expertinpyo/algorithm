import sys
sys.stdin = open('input.txt')

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
    while m:                                            # m시간만큼 확인
        dic = dict()                                    # 딕셔너리 생성
        for i in range(k):                              # k만큼 돌린다
            if arr[i][2]:                               # 미생물이 있을 때
                x, y = arr[i][0], arr[i][1]             # arr에서 x, y 꺼내오기
                nx, ny = x + direction[arr[i][3]][1], y + direction[arr[i][3]][0]   # 새로운 nx, ny 정의
                if (nx, ny) in dic:                     # 이 값이 dic에 있다면
                    dic[(nx, ny)].append([x, y, i])     # value 값에 append
                else:                                   # 아니라면
                    dic[(nx, ny)] = [[x, y, i]]         # key와 value 추가
        for key in dic:                                 # 딕셔너리 내 key들 반복문 실행
            if len(dic[key]) == 1:                      # 값이 하나일 때 이동과 값의 변화에 제한이 없으므로
                arr[dic[key][0][2]][0], arr[dic[key][0][2]][1] = key[0], key[1]     # x, y 값 업데이트
                if key[0] in [0, n-1] or key[1] in [0, n-1]:    # 미생물이 검역 구간 내 있다면
                    arr[dic[key][0][2]][2] //= 2                # 개수 0.5배(버림)
                    if arr[dic[key][0][2]][3] % 2:  # 방향 변경 상<->하 / 좌<->우
                        arr[dic[key][0][2]][3] += 1
                    else:
                        arr[dic[key][0][2]][3] -= 1
            else:                                       # 방문 점이 여러개일 때
                king = -100
                total = 0                               # 해당 점의 최종 값 변수 선언
                for j in range(len(dic[key])):          # value 의 개수만큼 반복문
                    total += arr[dic[key][j][2]][2]     # total에 미생물 수 추가
                    if arr[dic[key][j][2]][2] > king:   # king : 최대 미생물 수
                        num = dic[key][j][2]
                        king = arr[dic[key][j][2]][2]
                for j in range(len(dic[key])):          # 다시 한번 value 반복문 진행
                    if arr[dic[key][j][2]][2] != king:  # 최대 미생물 수 보다 작으면, 미생물 수 kill
                        arr[dic[key][j][2]][2] = 0
                arr[num][2] = total                     # 최대 미생물 수로 갱신
                arr[num][0], arr[num][1] = key[0], key[1]   # x, y 갱신

        m -= 1                                          # m -= 1
    ans = 0
    for i in range(k):
        ans += arr[i][2]
    print(f'#{tc} {ans}')                               # arr 리스트 내 살아있는 미생물 수 모두 합치기