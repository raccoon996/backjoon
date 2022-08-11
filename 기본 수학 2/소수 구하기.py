import sys
M, N = list(map(int, sys.stdin.readline().split(' ')))

# 에라토스테네스의 체 이용
temp_number = [True] * (N+1) # True이면 소수이다.
temp_number[0] = False  
temp_number[1] = False

max_divide_Primenum = int(N ** 0.5)

for i in range(2, max_divide_Primenum + 1): # 1 부터 시작하면 모든것이 소수가 아니게 된다.
    if temp_number[i] == True: # 소수의 배수이면 소수가 아니다.
        for j in range(i*2, N+1, i): # i*2는 소수이후 배수부터
            temp_number[j] = False

for i in range(M, N+1):
    if temp_number[i] == True:
        print(i)
    

# temp_number = []
# for i in range(N-M+1):
#     temp_1 = M + i
#     temp_number.append(str(temp_1))

# temp_number = []
# i = M
# while i >= M and i <= N:
#     prime_number = True
#     j = 2
#     test_num = i
#     if test_num > 1: # 1은 소수가 아니다.
#         while j < test_num/2: 
#             # 소수가 아닌것
#             if test_num % j == 0:
#                 prime_number = False
#                 break
#             j += 1
#         # 소수가 인것
#         if prime_number == True:
#             temp_number.append(test_num)
#             print(test_num)
#     i += 1
# for j in range(len(temp_number)):
#     print(temp_number[j])