# 한 점에서 시작한다
# 그 점에서 연결된 졈들을 하나씩 탐색하면서 나머지 점들의 연결 관계를 따진 후 최댓값을 갱신해준다
# 리스트를 하나 만들어서 이미 연결된 것들은 거를 수 있는 가지치기가 필요하다
# 연결된 점을 구할 때에 최댓값보다 작은 값이라면 그냥 거른다
import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, cnt):
    vvisted = [0] * (n+1)
    queue = deque()
    queue.append(int(x[0]))
    vvisted[int(x[0])] = 1
    while queue:
        if vvisted.count(1) == cnt:
            return True
        x = queue.popleft()
        arx = arr[x]
        for a in range(1, n+1):
            if a != i and arx[a] and not visited[a] and not vvisted[a]:
                vvisted[a] = 1
                queue.append(a)
    return False

n = int(input())
pnum = list(map(int, input().split()))
arr = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    input_list = list(map(int, input().split()))
    for ip in range(1, input_list[0]+1):
        arr[i][input_list[ip]] = pnum[input_list[ip]-1]

tsum = sum(pnum)
possible = []
impossible = []
ans = 10**6
if n == 2:
    ans = abs(pnum[1]-pnum[0])
else:
    for i in range(1, n+1):
        visited = [0] * (n + 1)
        visited[i] = 1
        for j in range(1, n+1):
            if arr[i][j] or j == i:
                visited[j] = 1
                st = ''
                num = 0
                for k in range(1, n + 1):
                    if not visited[k]:
                        st += str(k)
                    else:
                        num += pnum[k-1]

                mins = abs(tsum - 2*num)
                if st not in possible and st not in impossible and mins < ans:
                    check = bfs(st, len(st))
                    if check:
                        possible.append(st)
                        ans = mins
                    else:
                        impossible.append(st)
                # if j != i:
                #     visited[j] = 0
# 시작 지점을 st에서 시작해야할 것 같다.
if ans == 10**6:
    ans = -1
print(ans)