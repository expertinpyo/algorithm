N = int(input())
arr = []
for _ in range(N):
    ipt = input().split()
    arr.append(ipt[1::])
arr.sort()
for i in range(N):
    if not i:
        print(arr[i][0])
        for j in range(1, len(arr[i])):
            print('--'*j + arr[i][j])
    else:
        n = -1
        for j in range(len(arr[i])):
            if not arr[i-1][j] == arr[i][j]:
                n = j
                break
        for j in range(n, len(arr[i])):
            print('--' * j + arr[i][j])