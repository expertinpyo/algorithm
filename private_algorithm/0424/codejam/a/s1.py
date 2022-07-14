from itertools import permutations as pm
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    max_num = 0

    ccnt = 0
    pmlist = list(pm(arr, n))
    for p in pmlist:
        cnt = 0
        p = list(p)
        while True:
            if len(p) <= 1:
                break
            if max(p) < max_num:
                break
            left, right = p[0], p[1]
            mins = min(left, right)
            if mins >= max_num:
                p.pop(0)
                p.pop()
                cnt += 2
                max_num = max(left, right)
            else:
                if mins == left:
                    if right >= max_num:
                        cnt += 1
                        p.pop()
                        max_num = right
                else:
                    if left >= max_num:
                        cnt += 1
                        p.pop(0)
                        max_num = left
        ccnt = max(ccnt, cnt)
    print(f'Case #{tc}: {ccnt}')