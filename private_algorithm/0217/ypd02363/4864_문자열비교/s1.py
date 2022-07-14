import sys
sys.stdin = open("input.txt")

def bruteforce(p, t):
    i = j = 0
    while i < len(t):
        if p[j] != t[i]:
            i = i - j
            j = -1
        i += 1
        j +=1

        if j == len(p):
            return 1
    return 0


T = int(input())
for tc in range(1, T+1):
    pattern = input()
    target = input()
    print(f"#{tc} {bruteforce(pattern, target)}")
