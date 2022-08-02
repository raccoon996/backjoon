import sys
S = list(sys.stdin.readline())

S_maxchr = 0
for i in range(26):
    A_1 = chr(i+65)
    A_2 = chr(i+97)
    S_count_temp = S.count(A_1) + S.count(A_2)
    # S_count.append(S_count_temp)
    if S_count_temp > S_maxchr:
        S_maxchr = S_count_temp
        max_chr = i+65
    elif S_count_temp == S_maxchr:
        max_chr = 63
print(f'{chr(max_chr)}')

 

