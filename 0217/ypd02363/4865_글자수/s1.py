import sys
sys.stdin = open("input.txt")

def count_str(str1, str2):
    max_num = 0
    for i in str1:
        a = str2.count(i)
        if a > max_num:
            max_num = a
    return max_num

T = int(input())
for tc in range(1, T+1):
    str1 = list(input())
    str2 = list(input())
    print(f"#{tc} {count_str(str1, str2)}")