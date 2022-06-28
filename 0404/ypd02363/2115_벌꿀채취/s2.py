# 문제 접근 방법
# 완전탐색을 진행할 것
# 각 위치에서 M 크기의 영역에서 얻을 수 있는 최대 이익들을 다 구한 다음
# 구한 이익들의 조합을 다 따져보면 된다.
import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    n, m, c = map(int, input().split())                         # input
    arr = [list(map(int,input().split())) for _ in range(n)]    # 값들 input
    sake = [[0]*n for _ in range(n)]                            # n*n 빈 리스트
    for i in range(n):
        for j in range(0, n - m + 1):                           # 가로는 0부터 n-m번째 까지 확인
            ans = 0
            a = arr[i][j:j+m]                                   # 한 점에서 가질 수 있는 경우
            if sum(a) <= c:                                     # 이 값이 c보다 작거나 같은 경우
                for asd in a:                                   # 모든 원소들 제곱한 것 합
                    ans += asd**2
            else:                                               # sum 값이 c보다 큰 경우
                for k in range(1, (1 << m)-1):                  # 공집합과 모든 원소를 포함한 것을 제외한 부분집합 구하기
                    pp = []                                     # 생성할 부분집합을 담을 리스트
                    for p in range(m):
                        if k & (1 << p):
                            pp.append(a[p])                     # 리스트에 부분집합 원소들 담아주기

                    if sum(pp) <= c:                            # 부분집합 원소의 합이 c보다 작거나 같으면
                        mm = 0
                        for p in pp:                            # 모든 원소들 제곱해서 더해주기
                            mm += p**2
                    if ans < mm:                                # 그 더한 값들의 최댓값을 구해서 sake에 추가
                        ans = mm
            sake[i][j] = ans

    max1 = 0                                    # 최댓값 1 구하기
    for i in range(n):
        for j in range(n):
            if sake[i][j] > max1:
                max1 = sake[i][j]
                idx1 = [i, j]                   # 그 최댓값의 인덱스
    max2 = 0                                    # 최댓값 2 구하기
    for i in range(n):
        for j in range(n):
            if sake[i][j] > max2:
                if i == idx1[0] and abs(j-idx1[1]) <= m:    # 최댓값 2가 최댓값 1의 바로 옆에 있어 벌통이 겹치는 경우는 제외
                    continue
                else:
                    max2 = sake[i][j]
    print(f"#{tc} {max1 + max2}")               # 출력