import sys
sys.stdin = open('input.txt')



T = int(input())
for tc in range(1, T+1):
    f = float(input())
    a = 1
    s = ''
    while True:
        if len(s) > 12:
            s = 'overflow'
            break
        a /= 2
        if f >= a:
            s += '1'
            if f == a:
                break
            f -= a
        elif f < a:
            s += '0'

    print(f"#{tc} {s}")