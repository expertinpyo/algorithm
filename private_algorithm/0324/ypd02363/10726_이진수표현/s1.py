# 먼저 이진수로 만든다
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    bm = bin(m)[2:]
    switch = True
    if len(bm) < n:
        switch = False
    else:
        for i in range(-1, -1-n, -1):
            if bm[i] == '0':
                switch = False
                break
    if switch:
        print(f"#{tc} ON")
    else:
        print(f"#{tc} OFF")