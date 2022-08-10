import sys

N = []
while True:
    N_temp = int(sys.stdin.readline())
    if N_temp == 0:
        break
    N.append(N_temp)


for Num in range(len(N)):
    Num1 = N[Num]
    Num2 = N[Num] * 2
    N[Num] = 0
    # for i in range(Num2 - Num1):
    #     prime_number = True
    #     j = 2
    #     test_num = i
    #     if test_num > 1: # 1은 소수가 아니다.
    #         while j < test_num: 
    #             # 소수가 아닌것
    #             if test_num % j == 0:
    #                 prime_number = False
    #                 break
    #             j += 1
    #         # 소수가 인것
    #         if prime_number == True:
    #             N[Num] += 1
    #     else:
    #         N[Num] += 1
    # i += 1
