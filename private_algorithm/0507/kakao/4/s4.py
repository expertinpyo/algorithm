# n개의 지점
# 1부터 n까지 번호, 출입구/쉼터/산봉우리

# 양방향 통행 가능
# 등산로별로 이동시간 ㅇ존재
# 쉼터, 산봉우리 방문 시 휴식 가능
# 휴식없이 이동하는 시간 중 가장 긴 시기나 => intensity
# 산 봉우리 중 한 곳 방문
# 출입구 : 처음과 끝 한번씩, 산봉우리 한번
# intensity가 최소가 될 수 있도록 해야함


# 완전탐색 진행해야 함
# 지점 수 n / 등산로 정보 paths [i, j, w] / 출입구 gates / 산봉우리 번호 summits
# gates와 summits 아닌 점은 모두 쉼터
# 산봉우리 번호 and intensity의 최솟값 배출
# intensity가 여러개라면 산봉우리 번호 최소 값 출력


def solution(n, paths, gates, summits):
    answer = []
    lens = len(paths)



    for gate in gates:
        start = gate
        stack = [start]
        top = False
        while True:
            next = stack.pop()
            if next == start:
                pass
            for i in range(lens):
                s, e, roads = paths[i][0], paths[i][1], paths[2]
                if s == next:
                    if e not in gates:  # 시작점이 아니라면
                        if not top: # 봉우리에 방문한 적이 없다면

    return answer
