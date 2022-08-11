import sys

N = []
while True:
    N_temp = int(sys.stdin.readline())
    if N_temp == 0:
        break
    else:
        Num1 = N_temp
        Num2 = N_temp * 2 + 1

        # 에라토스테네스의 체 이용
        temp_number = [True] * (Num2) # True이면 소수이다.
        # 0 과 1은 소수에서 제외
        # temp_number[0] = False  
        # temp_number[1] = False

        max_divide_Primenum = int(Num2 ** 0.5)

        for i in range(2, max_divide_Primenum + 1): # 1 부터 시작하면 모든것이 소수가 아니게 된다.
            if temp_number[i] == True: # 소수의 배수이면 소수가 아니다.
                for j in range(i+i, Num2, i): # i*2는 소수이후 배수부터
                    temp_number[j] = False

        count = 0
        for i in range(Num1+1, Num2):
            if temp_number[i] == True:
                count += 1
        print(count)