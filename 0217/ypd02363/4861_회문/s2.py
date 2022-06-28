import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    # 회문이 가로에 있다고 가정
    sentence = ''
    for i in range(n):
        p = True
        for j in range(n - m + 1):
            for k in range(m // 2):
                if arr[i][k] != arr[i][-1 - k]:
                    p = False
                    break
            if p:
                sentence = arr[i]
                break
        if sentence:
            break
    # 회문이 가로에 없다면
    if not sentence:
        for i in range(n):
            p = True
            for j in range(n - m + 1):
                for k in range(m // 2):
                    if arr[k][i] != arr[-1 - k][i]:
                        p = False
                        break
                if p:
                    for d in range(n):
                        sentence += arr[d][i]
                    break

    print(f"{tc} {sentence}")