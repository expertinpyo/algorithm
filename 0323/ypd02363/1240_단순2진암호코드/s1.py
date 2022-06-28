# 총 8개의 숫자
# 앞 7자리는 상품 고유 번호, 마지막 자리는 검증 코드
# 검증코드 : 홀수자리합*3 + 짝수자리합 + 검증코드 = 10의 배수
# 스캐너 : 세로 50 가로 100 이하의 직사각형 배열
import sys
sys.stdin = open('input.txt')


code = [[[[[[[0 for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)]
code[0][0][0][1][1][0][1] = 0
code[0][0][1][1][0][0][1] = 1
code[0][0][1][0][0][1][1] = 2
code[0][1][1][1][1][0][1] = 3
code[0][1][0][0][0][1][1] = 4
code[0][1][1][0][0][0][1] = 5
code[0][1][0][1][1][1][1] = 6
code[0][1][1][1][0][1][1] = 7
code[0][1][1][0][1][1][1] = 8
code[0][0][0][1][0][1][1] = 9

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())    # 세로크기 n / 가로크기 m
    arr = [list(map(int, input())) for _ in range(n)]
    for i in range(n):
        a = arr[i]
        pos = -1
        ans = []
        for j in range(m-1, -1, -1):
            if a[j]:
                pos = j
                break
        while pos > 7:
            x = code[a[pos-6]][a[pos-5]][a[pos-4]][a[pos-3]][a[pos-2]][a[pos-1]][a[pos]]
            ans.append(x)
            pos -= 7
        if ans:
            odd = 0
            for o in range(7, 0, -2):
                odd += ans[o]
            even = 0
            for e in range(6, 1, -2):
                even += ans[e]
            if (odd*3 + even + ans[0]) % 10 == 0:
                print(f"#{tc} {sum(ans)}")
                break
    else:
        print(f"#{tc} {0}")