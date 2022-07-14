T = int(input())


for tc in range(1, T+1):
    r, c = map(int, input().split())
    first = '+-'
    second = '|.'
    print(f'Case #{tc}:')
    for i in range(r):
        if not i:
            print('..' + first * (c-1) + '+')
            print('..' + second * (c-1) + '|')
        else:
            print(first * c + '+')
            print(second * c + '|')
    print(first * c + '+')