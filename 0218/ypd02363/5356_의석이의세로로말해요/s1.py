import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    arr_h = [list(input()) for _ in range(5)]
    len_list = [len(arr_h[_]) for _ in range(5)]
    max_len = max(len_list)

    for i in range(5):
        if len(arr_h[i]) != max_len:
            while len(arr_h[i]) < max_len:
                arr_h[i].append('')
    arr_v = list(zip(*arr_h))
    sentence = ''
    for i in range(len(arr_v)):
        for j in arr_v[i]:
            sentence += j
    print(f"#{tc} {sentence}")