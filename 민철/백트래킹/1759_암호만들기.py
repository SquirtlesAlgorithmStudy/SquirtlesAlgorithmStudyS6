import itertools
import sys

L, C = map(int, sys.stdin.readline().split())
words = sorted(list(sys.stdin.readline().split()))

candidates = itertools.combinations(words, L)

for candidate in candidates:
    vowel = 0
    consonant = 0
    word = ''.join(candidate)
    for char in word:
        if char in 'aeiou':
            vowel += 1
        else:
            consonant += 1
    
    if vowel >= 1 and consonant >= 2:
        print(word)