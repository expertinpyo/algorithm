import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    for i in range(1, int(n**0.34)+1):
        if i ** 3 == n:
            print(f"#{tc} {i}")
            break
    else:
        print(f"#{tc} {-1}")