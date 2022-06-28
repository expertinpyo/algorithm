#5373
# 위 w 아래 y 앞 r 뒤 o 왼g 오b
# U  / D / F / B / L / R
U = ['w'] * 10
D = ['y'] * 10
F = ['r'] * 10
B = ['o'] * 10
L = ['g'] * 10
R = ['b'] * 10
dice = {
    'U': U,
    'D': D,
    'F': F,
    'B': B,
    'L': L,
    'R': R,
}
directions = {
    '1': [F, R, B, L],
    '2': [U, F, D, B],
    '3': [U, R, D, L],
}
n = int(input())
for _ in range(n):
    times = int(input())
    arr = list(input().split())
    for j in range(times):
        layer, direction = arr[j][0], arr[j][1]
        layer = dice[layer]
        if layer in [U, D]:
            dice_list = directions['1']
        elif layer in [F, B]:
            dice_list = directions['3']
        else:
            dice_list = directions['2']
        a, b, c, d = dice_list[0], dice_list[1], dice_list[2], dice_list[3]

        if layer == U:
            if direction == '-':
                for i in range(1, 4, 1):
                    a[i], b[i], c[i], d[i] = b[i], c[i], d[i], a[i]
            else:
                for i in range(1, 4, 1):
                    a[i], b[i], c[i], d[i] = d[i], a[i], b[i], c[i]

        elif layer == D:
            if direction == '-':
                for i in range(7, 10, 1):
                    a[i], b[i], c[i], d[i] = b[i], c[i], d[i], a[i]
            else:
                for i in range(7, 10, 1):
                    a[i], b[i], c[i], d[i] = d[i], a[i], b[i], c[i]

        elif layer == L:
            if direction == '-':
                for i in range(0, 3, 1):
                    a[i*3 + 1], b[i*3 + 1], c[i*3 + 1], d[9-i*3] = b[i*3 + 1], c[i*3 + 1], d[9-i*3], a[i*3 + 1]
            else:
                for i in range(0, 3, 1):
                    a[i*3 + 1], b[i*3 + 1], c[i*3 + 1], d[9-i*3] = d[9-i*3], a[i*3 + 1], b[i*3 + 1], c[i*3 + 1]

        elif layer == R:
            if direction == '+':
                for i in range(0, 3, 1):
                    a[i*3 + 3], b[i*3 + 3], c[i*3 + 3], d[7-i*3] = b[i*3 + 3], c[i*3 + 3], d[7-i*3], a[i*3 + 3]
            else:
                for i in range(0, 3, 1):
                    a[i*3 + 3], b[i*3 + 3], c[i*3 + 3], d[7-i*3] = d[7-i*3], a[i*3 + 3], b[i*3 + 3], c[i*3 + 3]

        elif layer == F:
            if direction == '-':
                for i in range(0, 3, 1):
                    a[i+7], b[i*3 + 1], c[i+1], d[9-i*3] = b[i*3 + 1], c[3-i], d[9-i*3], a[i+7]
            else:
                for i in range(0, 3, 1):
                    a[i+7], b[i*3 + 1], c[3-i], d[9-i*3] = d[9-i*3], a[i+7], b[i*3 + 1], c[i+1]

        else:
            if direction == '+':
                for i in range(0, 3, 1):
                    a[i+1], b[i*3 + 3], c[i+7], d[7-i*3] = b[i*3 + 3], c[9-i], d[i*3+1], a[i+1]
            else:
                for i in range(0, 3, 1):
                    a[i+1], b[i*3 + 3], c[i+7], d[7-i*3] = d[7-i*3], a[i+1], b[i*3 + 3], c[i+7]

    for x in range(1, 10, 3):
        print(U[x]+U[x+1]+U[x+2])
    print()





