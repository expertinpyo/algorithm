#5373
# 위 w 아래 y 앞 r 뒤 o 왼g 오b
# U  / D / F / B / L / R
def rotation(layer):
    box = [0] * 10
    if direction == '-':
        for i in range(0, 9, 1):
            if i // 3 == 0:
                box[i+1] = layer[3*(i + 1)]
            elif i // 3 == 1:
                box[i+1] = layer[3*(i - 3)+2]
            else:
                box[i+1] = layer[3*(i-6)+1]
    else:
        for i in range(0, 9, 1):
            if i // 3 == 0:
                box[i + 1] = layer[7 - 3 * i]
            elif i // 3 == 1:
                box[i + 1] = layer[8 - 3 * (i - 3)]
            else:
                box[i + 1] = layer[3 * (9 - i)]
    return box


n = int(input())
for _ in range(n):
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
        '1': [F, R, B, L],  # 상, 하
        '2': [U, F, D, B],  # 좌, 우
        '3': [U, R, D, L],  # 앞, 뒤
    }
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
            for i in range(3):
                if direction == '+': # 시계방향
                    a[i+1], b[i+1], c[i+1], d[i+1] = b[i+1], c[i+1], d[i+1], a[i+1]
                else:   # 반 시계방향
                    a[i+1], b[i+1], c[i+1], d[i+1] = d[i+1], a[i+1], b[i+1], c[i+1]



        elif layer == D:
            for i in range(3):
                if direction == '+': # 시계방향
                    a[i+7], b[i+7], c[i+7], d[i+7] = d[i+7], a[i+7], b[i+7], c[i+7]
                else:   # 반 시계방향
                    a[i+7], b[i+7], c[i+7], d[i+7] = b[i+7], c[i+7], d[i+7], a[i+7]



        elif layer == R:
            for i in range(3):
                if direction == '+': # 시계방향
                    a[i*3 + 3], b[i*3 + 3], c[i*3 + 3], d[7-3*i] = b[i*3 + 3], c[i*3 + 3], d[7-3*i], a[i*3 + 3]
                else:   # 반 시계방향
                    a[i*3 + 3], b[i*3 + 3], c[i*3 + 3], d[7-3*i] = d[7-3*i], a[i*3 + 3], b[i*3 + 3], c[i*3 + 3]



        elif layer == L:
            for i in range(3):
                if direction == '+':  # 시계방향
                    a[3*i + 1], b[3*i + 1], c[3*i + 1], d[9-3*i] = d[9-3*i], a[3*i + 1], b[3*i + 1], c[3*i + 1]
                else:  # 반 시계방향
                    a[3*i + 1], b[3*i + 1], c[3*i + 1], d[9-3*i] = b[3*i + 1], c[3*i + 1], d[9-3*i], a[3*i + 1]


        elif layer == B:
            for i in range(3):
                if direction == '+': # 시계방향
                    a[i+1], b[3*i+3], c[9-i], d[7-3*i] = b[3*i+3], c[9-i], d[7-3*i], a[i+1]
                else:   # 반 시계방향
                    a[i+1], b[3*i+3], c[9-i], d[7-3*i] = d[7-3*i], a[i+1], b[3*i+3], c[9-i]


        elif layer == F:
            for i in range(3):
                if direction == '+':  # 시계방향
                    a[7+i], b[3*i+1], c[3-i], d[9-3*i] = d[9-3*i], a[7+i], b[3*i+1], c[3-i]
                else:  # 반 시계방향
                    a[7+i], b[3*i+1], c[3-i], d[9-3*i] = b[3*i+1], c[3-i], d[9-3*i], a[7+i]

        box = rotation(layer)

        for i in range(1, 10):
            layer[i] = box[i]

        # print(U, D, F, B, L, R)

    for x in range(1, 10, 3):
        print(U[x]+U[x+1]+U[x+2])






