import sys
sys.stdin = open("input.txt")

def paper(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    if n >= 3:
        if n % 2:
            return 2 * paper(n-1) - 1
        else:
            return 2 * paper(n-1) + 1
T = int(input())
for tc in range(1, T+1):
    n = int(input()) // 10
    print(f"#{tc} {paper(n)}")

