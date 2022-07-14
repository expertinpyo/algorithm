from itertools import combinations as c
from itertools import permutations as p
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    fun = [0]+list(map(int, input().split()))
    fun_dic = dict()
    for f in fun:
        if f in fun_dic:
            fun_dic[f] += 1
        else:
            fun_dic[f] = 1
    module = [0] + list(map(int, input().split()))   # index control

    initiator = []
    for i in range(1, n + 1):
        if i not in module:
            initiator.append(i)
    c_list = list(c(fun, len(initiator)))
    cc = []
    for i in range(len(c_list)):
        c_list[i] = sum(list(c_list[i]))
    c_list = sorted(list(set(c_list)), reverse=True)


    p_list = list(p(initiator))
    maximum = False

    real_ans = 0
    for pp in p_list:
        visited = [0] * (n + 1)
        ans = 0
        for i in pp:
            start = i
            l = []
            while True:
                if not visited[start]:
                    visited[start] = 1
                    l.append(fun[start])
                    if not module[start]:
                        max_n = max(l)
                        ans += max_n
                        break
                    else:
                        start = module[start]
                else:
                    max_n = max(l)
                    ans += max_n
                    break

            if ans == c_list[0]:
                maximum = True
                break

        if real_ans < ans:
            real_ans = ans
        if maximum:
            break
    print(f"Case #{tc}: {real_ans}")