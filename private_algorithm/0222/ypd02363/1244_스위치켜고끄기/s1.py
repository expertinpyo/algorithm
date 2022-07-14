T = int(input())
arr = list(map(int, input().split()))
tc = int(input())
for tcc in range(tc):
    g, n = map(int, input().split())    # 인자들 입력받기
    if g == 1:                          # 남자면
        for i in range(T):
            if not (i+1) % n:           # n의 배수인 경우 바꿔주기
                if arr[i]:
                    arr[i] = 0
                else:
                    arr[i] = 1
    else:                               # 여자인 경우
        m = n-1
        j = 0
        while m-j >= 0 and m+j < T:     # m-j가 arr 인덱스 범위 내인 경우
            if arr[m-j] != arr[m+j]:    # 두(처음엔 한) 인자가 서로 다르면 반복문 종료
                break
            else:                       # 같다면 변경
                if arr[m-j]:
                    arr[m-j] = 0
                else:
                    arr[m-j] = 1
                arr[m+j] = arr[m-j]
            j += 1

for i in range(T):                  # 20개 넘으면 줄 바꿔가며 출력해주기
    print(arr[i], end=" ")
    if (i+1) % 20 == 0:
        print()

