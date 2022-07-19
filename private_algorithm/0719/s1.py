# 먼저 target에 해당하는 문자열이 있는지 확인
# 만약 target의 첫 단어가 나오나, 그 단어가 아닐 시 건너뛰어서 확인해보는 것도 좋을 듯.
string = input()
target = input()
stack = []
visited = [0] * (len(string))
for i in range(len(string)):
    if string[i] == target[0]:
        stack.append(i)
while stack:
    start = stack.pop()
    sen = ''
    btn = True
    for i in range(start, len(string)):
        if not visited[i]:
            sen += string[i]
        if not sen in target:
            btn = False
            break
        if len(sen) == len(target):
            break
    if btn:
        cnt = 0
        for i in range(start, len(string)):
            if not visited[i]:
                visited[i] = 1
                cnt += 1
            if cnt == len(target):
                break
if visited.count(1) == len(string):
    print("FRULA")
else:
    for i in range(len(string)):
        if not visited[i]:
            print(string[i], end='')
