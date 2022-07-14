# 길이 같은 두개 큐
# 하나 pop => 다른 큐에 insert
# 각 큐의 원소 합이 동일하게끔
# 이 작업의 최소 횟수
# pop and insert는 한번으로 카운트
#

from itertools import combinations as cb

def solution(queue1, queue2):
    cnt = 0
    answer = -2
    queue = queue1 + queue2
    total = sum(queue)
    n = len(queue) // 2
    q1 = list(range(n))
    q2 = list(range(n, 2*n))
    print(q1, q2)
    combis = list(cb(range(0, len(queue)), n))
    ans_list = []
    for combi in combis:
        compared = []
        for i in range(len(queue)):
            if i not in combi:
                compared.append(i)
        left, right = 0, 0
        for i in range(n):
            left += combi[i]
            right += compared[i]
        if left == right and combi not in ans_list:
            ans_list.append(list(combi))
    print(ans_list)
    if not ans_list:
        answer = -1
        return answer



solution([3, 2, 7, 2], [4, 6, 5, 1])