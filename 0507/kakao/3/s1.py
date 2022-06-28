def solution(alp, cop, problems):
    cnt = 0
    min_alp, min_cop = 10 ** 6, 10 ** 6
    max_alp, max_cop = 0, 0
    n = len(problems)
    for i in range(n):
        max_alp, max_cop = max(problems[i][0], max_alp), max(problems[i][1], max_cop)
        min_alp, min_cop = min(problems[i][0], min_alp), min(problems[i][1], min_cop)
    study_al = [0, 0, 1, 0, 1, 1, 0]
    study_co = [0, 0, 0, 1, 1, 0, 1]
    possible = []
    while True:
        if alp >= max_alp and cop >= max_cop:
            break

        if min_alp > alp or min_cop > cop:  # 첫번째
            if alp < min_alp:
                alp += 1
                cnt += 1
            else:
                cop += 1
                cnt += 1
            continue


        for problem in problems:
            if problem[0] <= alp and problem[1] <= cop and problem not in possible:
                possible.append(problem)
            else:
                min_alp, min_cop = min(problems[i][0], alp), min(problems[i][1], cop)   # 타겟 갱신

        if len(possible) == n:
            break

        for pos in possible:
            al = pos[2]
            co = pos[3]
            time = pos[4]
            pos.append(al/time)
            pos.append(co/time)


        goodal = 0
        goodco = 0
        idxal, idxco = -1, -1
        for i in range(len(possible)):
            comal = possible[i][-2]
            comco = possible[i][-1]

            if goodal < comal:
                goodal = comal
                idxal = i
            if goodco < comco:
                goodco = comco
                idxco = i

        if alp >= min_alp and cop < min_cop:
            if goodco < 1:
                cop += 1
                cnt += 1
            else:
                alp += possible[idxco][2]
                cop += possible[idxco][3]
                cnt += possible[idxco][4]
        elif cop >= min_cop and alp < min_alp:
            if goodal < 1:
                alp += 1
                cnt += 1
            else:
                alp += possible[idxal][2]
                cop += possible[idxal][3]
                cnt += possible[idxal][4]
        else:
            if goodal > goodco:
                alp += possible[idxal][2]
                cop += possible[idxal][3]
                cnt += possible[idxal][4]
            else:
                alp += possible[idxco][2]
                cop += possible[idxco][3]
                cnt += possible[idxco][4]

    answer = cnt
    print(answer)
    return answer
solution(

0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]])