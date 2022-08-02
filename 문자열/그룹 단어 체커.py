def group_word(word):
    temp_word = word
    word_alphabet = list(word)
    num = 0
    while num < len(word_alphabet):
        alphabet_len = len(temp_word) - len(temp_word.lstrip(word_alphabet[num]))
        temp_word = temp_word.lstrip(word_alphabet[num])
        alphabet_count= word.count(word_alphabet[num])
        if alphabet_len != alphabet_count:
            return 0
        else:
            num = num + alphabet_len
    return 1

import sys

N = int(sys.stdin.readline())

word = [sys.stdin.readline().strip() for i in range(N)] # N번 단어 입력

gorup_count = 0
for i in range(N):
    gorup_count += group_word(word[i])
print(gorup_count)

