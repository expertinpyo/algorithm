# 16가지 경우의 수
# n개의 질문 => 7개의 선택지

# 1가지 지표로 성격유형 점수 판단(-3~3)
# 하나의 지표에서 각 성격유형 점수가 동일하다면 사전순으로 빠른 성격유형을 선택
# survey 1차원 배열
# 정수배열 choices
# choices 길이 <= 7

# 1: R, T
# 2: C F
# 3: J M
# 4: A N
# 기준이 4
# 1부터 7까지 점수 매길 수 있음

def solution(survey, choices):
    ans_list = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    results = [[0, 0] for _ in range(4)]
    for i in range(len(survey)):
        left, right = survey[i][0], survey[i][1]
        if left in ['R', 'T']:
            idx = 0
        elif left in ['C', 'F']:
            idx = 1
        elif left in ['J', 'M']:
            idx = 2
        else:
            idx = 3

        if left == ans_list[idx][0]:
            iidx = 0
        else:
            iidx = 1

        point = choices[i]
        if not iidx:
            if point // 4:
                results[idx][1] += point % 4
            else:
                results[idx][0] += (4-point)
        else:
            if point // 4:
                results[idx][0] += point % 4
            else:
                results[idx][1] += (4-point)


    answer = ''
    for i in range(4):
        if results[i][0] >= results[i][1]:
            answer += ans_list[i][0]
        else:
            answer += ans_list[i][1]
    print(answer)
    return answer

solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])