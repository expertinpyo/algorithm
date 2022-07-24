def dfs(sen):
    global ans
    if len(sen) == N:
        ans = min(int(sen), ans)
        return
    if ans != float('inf'):
        if 10 ** (N - len(sen)) * int(sen) > ans:
            return
    for j in range(N//2):
        for k in range()


    for j in range(1, 4):
        if str(j) != sen[-1]:
            dfs(sen+str(j))

N = int(input())
ans = float('inf')
for i in range(1, 4):
    dfs(str(i))
print(ans)
