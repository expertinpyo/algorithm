import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())        # 화물 개수
    # 화물을 end값에 따라 정렬
    time = sorted([list(map(int, input().split())) for _ in range(n)], key = lambda x: x[1])
    print(time)
    maxs = -1            # 최대값 정의
    for i in range(n):  # 모든 화물에 대해
        if i <= maxs:   # i가 maxs보다 작으면 break
            break
        s = time[i]     # 초기값 설정
        tr = i + 1      # 초기값 + 1
        cnt = 1         # cnt 초기값, 1 (자기 자신을 포함)
        while tr < n:   # trial이 n보다 작을 때만 본다
            if time[tr][0] >= s[1]: # 초기값의 end(끝나는 시간)보다 그 다음값의 시작이 크거나 같은 경우
                cnt += 1            # cnt += 1
                s = time[tr]        # s는 time[tr]로 갱신
            tr += 1
        if maxs < cnt:              # max값 갱신
            maxs = cnt
    print(f"#{tc} {maxs}")
