from collections import deque
S = input()
T = input()
queue = deque([])
queue.append(S)
visited = [S]
ans = 0
while queue:
    word = queue.popleft()
    if word == T:
        ans = 1
        break
    word1 = word + 'A'
    word2 = word[::-1] + 'B'
    for i in [word1, word2]:
        if i not in visited:
            visited.append(i)
            queue.append(i)
print(ans)