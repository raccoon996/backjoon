import sys
word = sys.stdin.readline().strip() # 단어 입력

Croatian_Alphabet = ["c=", "c-", "dz=", "d-",
        "lj", "nj", "s=", "z="] # 크로아티아 알파벳

count_num = 0 
for i in range(8): # 크로아티아 알파벳 개수 만큼
    temp_Croatian = Croatian_Alphabet[i] 
    count_num += word.count(temp_Croatian) # 특정 크로아티아 알파벳 개수 찾기
    word = word.replace(temp_Croatian, " ") # 찾은 크로아티아 알파벳 제거
count_num += len(word.replace(" " ,"")) # 보통 알파벳 개수 카운트

print(f'{count_num}')

