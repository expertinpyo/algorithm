# Trie 문제
# 백준 14725
# 더 이상 내려갈 수 없으면 멈추고 신호를 보냄
# 먹이 정보 개수 N개
# 로봇 개미 한마리가 보내준 먹이 정보 개수 K
# 로봇 개미가 왼쪽부터 순서대로 각 층 마다 지나온 방에 있는 먹이 정보
# 여러 개의 방이 있을 때는 "사전" 순서대로

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