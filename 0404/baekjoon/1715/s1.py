# merge sort의 느낌이 난다
def card(ar):
    ans = 0
    l = []
    if len(ar) % 2:
        ar.append(0)
    while len(ar) > 2:
        for i in range(0, len(ar), 2):
            l.append(ar[i] + ar[i+1])
            ans += ar[i] + ar[i+1]
        ar = sorted(l)
    return sum(l)


n = int(input())
arr = [0]*n
for _ in range(n):
    arr[_] = int(input())
arr = sorted(arr)
print(card(arr))
