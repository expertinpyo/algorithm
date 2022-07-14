import sys
sys.stdin = open('input.txt')

T = int(input())
for i in range(1, T+1):
    k, n, m = map(int, input().split())
    station = [0]*(n+1)
    for j in list(map(int, input().split())):
        station[j] = 1
    location = 0
    charge = 0
    while location + k < n:
        for x in range(k, 0, -1):
            if station[location + x]:
                location += x
                charge += 1
                break
        else:
            charge = 0
            break

    print(f"#{i} {charge}")