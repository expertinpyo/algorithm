from copy import copy
N, K = map(int, input().split())
arr = list(map(int, input().split()))
belt = [0] * (2*N)
robot = [0] * N
cnt = 0
ans = 0
while cnt < K:
    # 1. 한바퀴 다 돔
    for i in range(N-1, 0, -1):
        belt[i] = arr[i-1]
        robot[i] = robot[i-1]
    for i in range(2*N-1, N-1, -1):
        belt[i] = arr[i-1]
    belt[0] = arr[2*N-1]
    robot[0] = 0
    robot[N-1] = 0
    # # 2. 가장 먼저 올라간 벨트부터 돈다
    for i in range(N-2, 0, -1):
        if robot[i] and belt[i+1] and not robot[i+1]:
            belt[i+1] -= 1
            robot[i+1] = robot[i]
            robot[i] = 0
            if i + 1 == N-1:
                robot[i+1] = 0
    if not robot[0] and belt[0]:
        robot[0] = 1
        belt[0] -= 1

    arr = copy(belt)
    ans += 1
    cnt = belt.count(0)
print(ans)