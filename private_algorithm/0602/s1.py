# swea 1865
# 순열을 통해서 문제에 접근할 수도 있으나 썩 좋은 방법은 아닌 것 같음
# N 이 특정 숫자 이상인 경우에는 메모리 초과 에러가 발생한다
# 따라서 dp 문제처럼 접근 해보자
# 완전탐색 문제
# 전체를 다 볼 필요는 없다
# 스테이지 처럼 생각을 해보는 것도 좋은 것 같다
# 재귀로 접근했다


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = []
    for _ in range(n):
        a = list(map(int, input().split()))
        arr.append(a)

    ranking = [[1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            cnt = 1
            for k in range(n):
                if j != k and arr[i][j] < arr[i][k]:
                    cnt += 1
            ranking[i][j] = cnt
    start = 0
    ans = 1

    \





    
