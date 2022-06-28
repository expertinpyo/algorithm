# 연속인 숫자가 3개 이상이면 run
# 같은 숫자가 3개 이상이면 triplet
# 무승부면 0 출력

import sys
sys.stdin = open("input.txt")

def babyjin(li):
    if li.count(3):                             # 3개인 원소가 있으면 True
        return True
    for ll in range(8):
        if li[ll]:
            if li[ll] and li[ll+1] and li[ll+2]: # 연속된 숫자가 있으면 True
                return True
    return False


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    one = []
    two = []
    for i in range(6):
        one.append(arr[2*i])
        two.append(arr[2*i+1])
        o = babyjin(one)
        t = babyjin(two)
        if o or t:
            if o and t:
                print(f"#{tc} {0}")
                break
            else:
                if o:
                    print(f"#{tc} {1}")
                else:
                    print(f"#{tc} {2}")
                break
    else:
        print(f"#{tc} {0}")
