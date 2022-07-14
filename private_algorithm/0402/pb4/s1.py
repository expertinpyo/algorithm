from itertools import combinations as c
from itertools import permutations as p
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    fun = list(map(int, input().split()))
    module = [0] + list(map(int, input().split()))
    visited = [0] * (n+1)
    initiator = []
    max_m = max(module)
    for i in range(1, n+1):
        if i not in module:
            initiator.append(i)
    print(initiator)
    print("module: ", module)
    # 큰 것은 고려하지 않아도 된다
    # 어차피 더해진느 값임
    # 그러면 최솟값 위주로 접근해야 한다
    cc = c(fun, len(initiator))
    c_list1 = cc
    c_list2 = list(p(initiator))
    print(c_list1)
    print(c_list2)
    # 1. 이니시에이터 찾기
    # 2. 최솟값 경우 찾기 = > 완전탐색이나 그리드로 점근
    # 탐색 과정에서 visited를 사용해서 도착한 경우는 인덱스를 바꿔준다