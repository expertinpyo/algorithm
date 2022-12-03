import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    commands = input().rstrip()
    n = int(input())
    arrays = input().rstrip()
    if commands.count("D") > n:
        print("error")
        continue    # D 개수가 배열 크기보다 클 시
    elif not n:
        print([])
    else:
        arrays = list(map(int, arrays[1:-1].split(",")))
        front = 0
        back = len(arrays) - 1
        cnt = 0
        reverse = False
        for command in commands:
            if command == "D":
                if cnt and cnt % 2:
                    reverse = False if reverse else True
                cnt = 0
                if reverse:
                    back -= 1
                else:
                    front += 1
            else:
                cnt += 1

        if cnt and cnt % 2:
            reverse = False if reverse else True

        if reverse:
            if front:
                arrays = arrays[back:front-1:-1]
            else:
                arrays = arrays[back::-1]

        else:
            arrays = arrays[front:back+1]
        ans = "["
        for i in range(len(arrays)):
            ans += str(arrays[i])
            if i != len(arrays) - 1:
                ans += ","
        ans +="]"

        print(ans)
