T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(3)]
    mins = [-1] * 4
    for i in range(3):
        for j in range(4):
            if mins[j] < 0:
                mins[j] = arr[i][j]
            else:
                mins[j] = min(mins[j], arr[i][j])
    if sum(mins) < 10**6 :
        print(f"Case #{tc}: IMPOSSIBLE")
    elif sum(mins) == 10 ** 6:
        print(f"Case #{tc}:", *mins)
    else:
        minus = sum(mins) - 10 ** 6
        for i in range(4):
            if mins[i] - minus >= 0:
                mins[i] -= minus
                break
            else:
                while mins[i]:
                    mins[i] -= 1
                    minus -= 1
                if not minus:
                    break
        print(f"Case #{tc}:", *mins)