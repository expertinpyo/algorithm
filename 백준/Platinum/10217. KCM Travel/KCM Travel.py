from collections import deque
def solution():
    T = int(input())
    for tc in range(T):
        n, m, k = map(int, input().split())
        arr = [[] for _ in range(n+1)]
        for _ in range(k):
            u, v, c, d = map(int, input().split())
            arr[u].append((v, c, d))
        inf = float('inf')
        dp = [[inf] * (m+1) for _ in range(n+1)]
        queue = deque()
        queue.append((0, 0, 1))
        while queue:
            time, cost, airport = queue.popleft()
            if time <= dp[airport][cost]:
                dp[airport][cost] = time
                for new_a, new_c, new_t in arr[airport]:
                    total_c = new_c + cost
                    total_t = new_t + time
                    if total_c <= m and total_t < dp[new_a][total_c]:
                        for i in range(total_c, m+1):
                            if dp[new_a][i] > total_t:
                                dp[new_a][i] = total_t
                            else:
                                break
                        queue.append((total_t, total_c, new_a))
        ans = min(dp[n])
        if ans == inf:
            print('Poor KCM')
        else:
            print(ans)

solution()