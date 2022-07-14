from itertools import combinations as cb

def sol():
    idx = 2*n-1
    tr = 0
    while True:
        if idx == 2*n-1:
            ar = arr[:idx:]
        else:
            ar = arr[:idx:] + arr[idx] + arr[idx+1::]

        if not tr:
            if arr[idx] == sum(ar):
                return arr[idx]
        else:
            ar2 = list(cb(ar, tr))
            for a in ar2:
                if (sum(a) + arr[idx]) * 2 == sum(arr):
                    ans = []
                    for ii in a:
                        ans.append(ii)
                    return ans + [arr[idx]]
        if tr == len(ar):
            idx -= 1
            tr = 0
        else:
            tr += 1

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    pos = True
    for aarr in [arr1, arr2]:
        for i in range(n):
            if aarr[i] > 10**9 or aarr[i] < 1:
                pos = False
        if len(list(set(aarr))) != n:
            pos = False
    if pos:
        arr = sorted(arr1 + arr2)
        print(sol())

