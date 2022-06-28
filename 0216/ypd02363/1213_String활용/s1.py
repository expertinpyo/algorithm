import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

for tc in range(10):
    T = int(input())
    pattern = input()
    target = input()
    m = len(pattern)
    n = len(target)
    i = j = 0
    ans = 0
    while i < n:
        p = pattern[j]
        t = target[i]
        if p != t:
            i = i - j
            j = -1

        i += 1
        j += 1
        if j == m:
            ans += 1
            j = 0

    print(f"#{T} {ans}")
