def solve(word):
    word_li = list(word)
    for i in range(len(word)//2):
        front = word_li[i]
        word_li[i] = word_li[len(word)-1-i]
        word_li[len(word)-1-i] = front

    word = "".join(word_li)
    return word

import sys
sys.stdin = open('input.txt')

#1. 반복문 활용
word = input()
print(solve(word)) # edcba

#2. pythonic (slicing)
word2 = input()
word2 = word2[::-1]
print(word2) # sgnirts siht esreveR
