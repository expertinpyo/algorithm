import sys
sys.stdin = open("input.txt")

for tc in range(10):
    T = int(input())
    arr1 = [input() for _ in range(100)]
    arr2 = [0] * 100
    for i in range(100):
        sentence = ''
        for j in range(100):
            sentence += arr1[j][i]
        arr2[i] = sentence
    # arr1 가로 / arr2 세로
    # 인덱스 접근으로 해결할 예정
    # 3중 for문, i : arr의 인덱스 접근
    # j : arr[i]의 인덱스
    # k : 회문의 길이 추적
    # 회문 1 : arr[i][j:j+k+1:1] j부터 j+k 까지
    # 회문 2 : arr[i][j+k:j-1:-1] j+k부터 j까지
    ans_list = [1]
    for i in range(100):
        for j in range(100):
            for k in range(99-j, 0, -1):
                original1 = arr1[i][j:j + k + 1:1]
                if j == 0:
                    reverse1 = arr1[i][j+k::-1]
                else:
                    reverse1 = arr1[i][j+k:j-1:-1]
                if original1 == reverse1:
                    ans_list.append(k+1)
                    break
        for j in range(100):
            for k in range(99-j, 0,-1):
                original2 = arr2[i][j:j + k + 1:1]
                if j == 0:
                    reverse2 = arr2[i][j+k::-1]
                else:
                    reverse2 = arr2[i][j+k:j-1:-1]
                if original2 == reverse2:
                    ans_list.append(k+1)

                    break

    print(f"#{T} {max(ans_list)}")
