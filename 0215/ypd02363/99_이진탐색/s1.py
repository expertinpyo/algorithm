# 이진 탐색 기본
import sys
sys.stdin = open("input.txt")

def binary_search(numbers, target):
   start = 0
   end = len(numbers) - 1
   while start <= end:
       mid = (end + start) // 2
       if numbers[mid] == target:
           return True
       else:
           if numbers[mid] < target:
               start = mid + 1
           else:
               end = mid - 1
   return False


numbers = list(map(int, input().split()))
print(binary_search(numbers, 5)) # True
print(binary_search(numbers, 10)) # False

