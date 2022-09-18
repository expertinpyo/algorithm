# 5639 이진검색트리
# 후위 순회한 결과
# 첫번째를 그렇게 다가가는 것도 괜찮다고는 생각한다.
n = int(input())
dic = {}
for _ in range(n):
    arr = list(input().split())
    if arr[1] not in dic:
        dic[arr[1]] = []
    for i in range(2, int(arr[0])+1):
        dic[arr[1]].append('-' * i + arr[i])
print(dic)
pre = sorted(dic)
for p in pre:
    print(p)
    for value in dic[p]:
        print(value)