# 알고리즘 지식 and 코드 구현
# 알고리즘 지식 = 알고력
# 코드 구현 = 코딩력

# 같은 문제 여러번 푸는 것 가능
# 모든 문제를 풀 수 있는 알고력, 코딩력을 얻는데 걸리는 최단시간을 return


def solution(alp, cop, problems):
    answer = 0
    alp, cop = alp, cop
    cnt = 0
    solved = []
    possible = []
    while True:
        if len(solved) == len(problems):
            answer = cnt
            return answer
        for i in range(len(problems)):
            alp_req, cop_req = problems[i][0], problems[i][1]
            if alp >= alp_req and cop >= cop_req:
                possible.append(i)

        for i in range(len(possible)):


