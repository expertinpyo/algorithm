# 사전학적으로 먼저 오는 경우를 계산해라
# 모든 경우가 있을 수 있다.
# 그 경우를 다 조사해서 진행할 것

def convert():
    idx = 0
    idx2 = 0
    s = a
    while idx < len(a):
        si = a[idx]
        if not idx:
            c1 = s
            c2 = s[idx2]*2 + s[idx2+1::]
        else:
            c1 = s[0:idx2:] + si + s[idx2+1::]
            c2 = s[0:idx2:] + si*2 + s[idx2+1::]
        li = [c1, c2]
        s = sorted(li)[0]
        idx += 1
        if s == c1:
            idx2 += 1
        else:
            idx2 += 2


    return s
T = int(input())
for tc in range(1, T+1):
    a = input()
    ans = []
    print(f"Case #{tc}: {convert()}")