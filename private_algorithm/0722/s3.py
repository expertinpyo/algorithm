# 2661
def dfs(x):
    global ans
    # 일정 값보다 더 클 때
    if ans != float('inf'):
        if int(x) * 10 ** (N-len(x)) > ans:
            return
    length = 2
    idx = 0
    while length <= len(x) // 2:
        if x[idx:idx+length] == x[idx+length:idx+length*2]:
            return
        idx += 1
        if idx + length*2-1 > len(x)-1:
            length += 1
            idx = 0

    if len(x) == N:
        ans = min(ans, int(x))
        return

    for j in range(1, 4):
        if str(j) != x[-1]:
            dfs(x+str(j))

N = int(input())
ans = float('inf')
for i in range(1,4):
    dfs(str(i))
print(ans)