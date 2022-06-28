# 이진 탐색 재귀
import sys
sys.stdin = open("input.txt")

def recursive_binary_search(numbers, low, high, target):
    if low > high:
        return False
    mid = (low + high) // 2
    if numbers[mid] == target:
        return True
    else
        if numbers[mid] < target:
            return recursive_binary_search(numbers, mid+1, high,target)
        else:
            return recursive_binary_sear:ch(numbers, low, mid-1,target)
    return False


numbers = list(map(int, input().split()))
print(recursive_binary_search(numbers, 0, len(numbers)-1, 5)) # True
print(recursive_binary_search(numbers, 0, len(numbers)-1, 10)) # False