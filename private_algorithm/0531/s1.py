# 6월 한 달 동안 단기간 성장 문제를 모두 풀어볼까 합니다
# 좋은 도전이 될 것 같아요
# 아 정말 재밌다 이거 진짜 하는거

# 12865 평범한 배낭

# n개의 물건 w 무게 v 가치
# 최대 k만큼의 무게만을 넣을 수 있음

N, K = map(int, input().split())
arr = []
for _ in range(N):
    W, V = map(int,input().split())
    if W <= K:
        arr.append((W, V))
ans = 0
for i in range(1 << len(arr)):
    w = 0
    v = 0
    btn = True
    for j in range(len(arr)):
        if i & (1 << j):
            if w + arr[j][0] <= K:
                w += arr[j][0]
                v += arr[j][1]
            else:
                btn = False
                break
    if btn:
        ans = max(ans, v)

print(ans)