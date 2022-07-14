import sys
sys.stdin = open("input.txt")

def bruteforce(p, t):
    i = j = cnt = 0
    while i < len(t):
        if p[j] != t[i]:
            i = i - j
            j = -1
        i += 1
        j += 1

        if j == len(p):
            cnt += 1
            j = 0

    return cnt


T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    num = bruteforce(B, A)
    print(f"#{tc} {len(A) - len(B)*num + num}")