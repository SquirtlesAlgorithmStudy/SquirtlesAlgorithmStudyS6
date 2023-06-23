import sys
input = sys.stdin.readline

L, C = map(int, input().split())
characters = list(input().rstrip().split())


def is_vowel(char):
    if char in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False


def discriminator(consonant_count, vowel_count, password):
    global L
    if (L-vowel_count) == 1:
        return True
    if len(password) == L:
        if consonant_count >= 2 and vowel_count >= 1:
            print(password)
            return True
        else:
            return True
    else:
        return False


def char2next(characters):
    global C
    result = {}
    characters.sort()
    for idx, char in enumerate(characters):
        if idx + 1 != C:
            result[char] = (characters[idx + 1:], list(range(C-idx-2, 0, -1)))
        else:
            result[char] = ([], [])
    return result


def dfs(char, password, consonant_count, vowel_count):
    global L
    global next_letter
    if is_vowel(char):
        vowel_count += 1
    else:
        consonant_count += 1
    password += char
    if discriminator(consonant_count, vowel_count, password):
        return
    else:
        next = next_letter[char]
        for char, remain_count in zip(*next):
            if remain_count + len(password) + 1 > L:
                dfs(char, password, consonant_count, vowel_count)


next_letter = char2next(characters)
for char, remain_count in zip(characters, list(range(C-1, 0, -1))):
    if remain_count + len("") + 1 > L:
        dfs(char, "", 0, 0)
