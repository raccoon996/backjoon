import sys
R = int(sys.stdin.readline())

S = [list(sys.stdin.readline()) for i in range(R)]#STR을 List로 만들기

for i in range(R): 
     repeat = int(S[i][0])
     for j in range(len(S[i])-3):
          str_repeat = S[i][j+2]
          for re in range(repeat):
               print(f'{str_repeat}',end='')
     print(f'\n',end='')