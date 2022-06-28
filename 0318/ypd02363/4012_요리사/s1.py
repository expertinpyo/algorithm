from itertools import combinations

def summ(li):
    ans = 0
    for i in li:
        x, y = i
        ans += (arr[x-1][y-1] + arr[y-1][x-1])
    return ans

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    num = n // 2
    arr = [list(map(int, input().split())) for _ in range(n)]
    num_list = list(range(1, n+1))
    combination = list(combinations(num_list, num))
    a = []
    for combi in combination:
        combi = list(combi)
        if combi[0] != 1:
            break
        else:
            a.append(combi)
    anss = []
    for i in a:
        b = []
        for j in num_list:
            if j not in i:
                b.append(j)
        ans_a = 0
        combi_a = summ(list(combinations(i, 2)))
        combi_b = summ(list(combinations(b, 2)))
        anss.append(abs(combi_a-combi_b))
    print(f"#{tc} {min(anss)}")
