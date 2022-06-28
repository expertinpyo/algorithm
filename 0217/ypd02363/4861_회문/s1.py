import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    # 회문이 가로에 있다고 가정
    sentence = ''
    for i in range(n):
        for j in range(n - m + 1):
            p = True
            for k in range(m // 2):
                if arr[i][j + k] != arr[i][m + j - 1 - k]:
                    p = False
                    break
            if p:
                sentence = arr[i][j:]
                break
        if sentence:
            break
    # 회문이 가로에 없다면
    if not sentence:
        for i in range(n):
            for j in range(n - m + 1):
                p = True
                for k in range(m // 2):
                    if arr[j + k][i] != arr[m + j - 1 - k][i]:
                        p = False
                        break
                if p:
                    for d in range(j, n):
                        sentence += arr[d][i]
                    break

    print(f"#{tc} {sentence}")