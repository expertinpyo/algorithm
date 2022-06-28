# 화물도크
# 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하는 경우
# 몇 대의 화물차가 이용할 수 있는지
import sys
sys.stdin = open('input.txt')

def dock(s):
    global end, cnt, mins
    if s == len(tm_list):
        if cnt > mins:
            mins = cnt
        return
    else:
        for ss in range(s, len(tm_list), 1):
            if end <= tm_list[ss][0]:
                previous_end = end
                end = tm_list[ss][1]
                cnt += 1
                dock(ss+1)
                end = previous_end
                cnt -= 1
            else:
                dock(ss+1)

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    time = sorted([list(map(int, input().split())) for _ in range(n)])
    start = end = mins = 0
    for t in range(n):
        cnt = 0
        tm_list = [time[t]]
        for tm in range(t, n):
            if time[t][1] <= time[tm][0]:
                tm_list.append(time[tm])
        if len(tm_list) <= mins:
            break
        dock(t) # 그 다음의 경우를 볼 수 있는 것을 구축해야 한다
    print(f'#{tc} {mins}')