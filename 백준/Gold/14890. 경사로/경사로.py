def is_possible(arr):
    visited = [[0] * N for _ in range(N)]
    ans = 0
    for i in range(N):
        go = True
        cnt = True
        for a in range(1, 11):
            if arr[i].count(a) == N:
                ans += 1
                go = False
                break
            elif arr[i].count(a):
                break
        if go:
            for j in range(N - 1):
                if arr[i][j] == arr[i][j + 1]:
                    continue
                elif abs(arr[i][j] - arr[i][j + 1]) >= 2:
                    cnt = False
                    break
                else:
                    if arr[i][j] > arr[i][j + 1]:  # 내려가는 경우
                        for k in range(j + 1, j + L + 1):
                            if k >= N or arr[i][k] != arr[i][j + 1] or visited[i][k]:
                                cnt = False
                                break
                            visited[i][k] = 1
                    else:  # 올라가는 경우
                        for k in range(j - L + 1, j + 1):
                            if k < 0 or arr[i][k] != arr[i][j] or visited[i][k]:
                                cnt = False
                                break
                            visited[i][k] = 1
                if not cnt:
                    break
            if cnt:
                ans += 1
    return ans

N, L = map(int, input().split())
first = [list(map(int, input().split())) for _ in range(N)]
second = list(zip(*first))
is_possible(second)
print(is_possible(first) + is_possible(second))




