"""
2. bfs - 인접 리스트 구현
"""
def bfs(v):
    queue = []
    queue.append(v)
    visited[v] = 1
    while queue:
        v = queue.pop(0)
        for x in range(1, V+1):
            if arr[v][x] == 1 and not visited[x]:
                visited[x] = visited[v] + 1
                queue.append(x)
import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())
# 간선 정보 초기화
nums = list(map(int, input().split()))
# Graph 초기화
arr = [[0]*E for _ in range(E)]
for i in range(E):
    arr[nums[i*2]][nums[i*2+1]] = 1
    arr[nums[i*2+1]][nums[i*2]] = 1
# 방문 표시 초기화
visited = [0]*E
# bfs 탐색 시작
bfs(1)
print(visited)