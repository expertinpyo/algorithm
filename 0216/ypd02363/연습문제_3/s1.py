def solve(word):
    if not word:
        return word
    last = word[-1]
    new_word = ''
    new_word += last
    next_word = word[0:len(word)-1]
    return last + solve(next_word)

import sys
sys.stdin = open('input.txt')

word1 = input()
word2 = input()
word3 = input()

print(solve(word1)) # otamot
print(solve(word2)) # ananab
print(solve(word3)) # oypnI
