def counting(li):
    # 1) 카운팅 하기
    cnt_list = [0]*10
    for i in range(len(li)):
        cnt_list[li[i]] += 1
    # 2) 누적합
    print(cnt_list)
    for i in range(1, len(cnt_list)):
        cnt_list[i] = cnt_list[i]+ cnt_list[i-1]
    print(cnt_list)
    # 3) 자리 찾기
    ans_list = [0]*len(li)
    for i in range(len(li)-1, -1, -1):
        ans_list[cnt_list[li[i]]-1] = li[i]
        cnt_list[li[i]] -= 1
    print(ans_list)

counting([5,0,5,0,4,1,4,3,4,4,0,4,0,2,3,5])