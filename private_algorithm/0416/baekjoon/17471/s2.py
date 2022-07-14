# 로직
# 먼저 모든 조합에 대해 따져보기(절반까지의)
# 그 이후 각 조합별 합을 구한 후 최솟값이 될 수 있는 조건인지 따져보기
# 조건에 해당 된다면 각 지점이 연결되어있는지 따져보기
# 연결되어있다면 최솟값 갱신해주기
from collections import deque
from itertools import combinations as cb
from copy import deepcopy
import sys
input = sys.stdin.readline


def connections():
    xlist = included
    ylist = []
    for num in range(1, n+1):
        if num not in xlist:
            ylist.append(num)

    if checking(xlist):
        final = checking(ylist)
        if final:
            return True
    return False

def checking(li):
    queue = deque([li[0]])
    anss = 1
    while queue:
        x = queue.popleft()
        if not for_check[x]:
            for_check[x] = 1

        if anss == len(li):
            return True

        arrr = arr[x]
        for ar in arrr:
            if not for_check[ar] and ar in li:
                queue.append(ar)
                anss += 1
    return False


n = int(input())
pnum = [0] + list(map(int, input().split()))
arr = [[]*(n+1) for _ in range(n+1)]
zero_cnt = 0
for i in range(1, n+1):
    input_list = list(map(int, input().split()))
    for ip in range(1, len(input_list)):
        arr[i].append(input_list[ip])

if n == 2:
    print(abs(pnum[1]-pnum[2]))
else:
    ans = sum(pnum) # 초기 값
    r_list = list(range(1, n + 1))
    for i in range(1, n//2 + 1):
        combi = list(cb(r_list, i))
        for com in combi:
            sums = 0
            included = []
            for_check = [0] * (n+1)
            for c in range(len(com)):
                sums += pnum[com[c]]
                included.append(com[c])
            if abs(sums*2- ans) < ans:
                if connections():          # 연결확인하기
                    ans = abs(sums*2- ans)
    if ans == sum(pnum):
        ans = -1
    print(ans)