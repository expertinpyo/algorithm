import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    num = int(input())
    a = b = c = d = e = 0
    num_list = [2, 3, 5, 7, 11]
    while num > 1:
        for i in num_list:
            if num % i:
                num_list.pop(num_list.index(i))
            else:
                if i == 2:
                    a += 1
                elif i == 3:
                    b += 1
                elif i == 5:
                    c += 1
                elif i == 7:
                    d += 1
                else:
                    e += 1
                num = num // i
    print(f"#{tc}",a, b, c, d, e)