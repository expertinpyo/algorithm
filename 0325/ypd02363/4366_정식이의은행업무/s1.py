def convert_2():
    ans = 0
    for i in range(len(second)):
        ans += second[i] * 2**(len(second)-1-i)
    return ans


def convert_3():
    ans = 0
    for i in range(len(third)):
        ans += third[i] * 3**(len(third)-1-i)
    return ans


T = int(input())
for tc in range(1, T+1):
    second = list(map(int, input()))                # 2진법 수
    third = list(map(int, input()))                 # 3진법 수
    answer = 0
    end = False                                     # 반복문 끝났는지 여부
    for sec in range(len(second)):                  # second 길이만큼 반복문
        if end: break                               # 끝났으면 반복문 종료
        else:
            origin_2 = second[sec]                  # second의 한 요소 바꾸기 전 초기값
            if second[sec]:                         # 값이 1이면 0으로 변환
                second[sec] = 0                     # 값이 0이면 1로 변환
            else:
                second[sec] = 1
            for thr in range(len(third)):           # third 길이만큼 반복문
                if end:                             # 끝났으면 end
                    break
                else:
                    origin_3 = third[thr]           # third의 한 요소 바꾸기 전 초기값
                    for th in range(3):             # 0~2까지 변할 수 있는 요소
                        third[thr] = th             # 한 요소 바꾸기
                        if convert_2() == convert_3():  # 바꾼 값이 서로 같다면
                            end = True                  # end = True
                            answer = convert_2()        # ans에 값 담기
                            break
                    third[thr] = origin_3           # 바꾼 값 초기값으로 변환
            second[sec] = origin_2                  # 바꾼 값 초기값으로 변환

    print(f"#{tc} {answer}")