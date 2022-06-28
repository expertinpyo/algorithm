import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    n, q = map(int, input().split())
    # q 회 동안 일정 범위의 연속한 상자를 동일한 숫자로 변경
    # i번째 작업에 대해 L번 상자부터 R번 상자까지의 값을 i로 변경
    # q 회 동안 위의 작업을 순서대로 한 다음 N개의 상자에 적혀있는 갓들을 순서대로 출력
    trial = []
    for i in range(q):
        trial.append(list(map(int, input().split())))
    box = [0] * n # n개의 숫자 박스
    for i in range(q):
        l, r = trial[i]
        for j in range(l, r+1):
            box[j-1] = i+1
    print("#{0}".format(tc), *box)
