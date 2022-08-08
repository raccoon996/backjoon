import sys
# M = int(sys.stdin.readline())
# N = int(sys.stdin.readline())
M = 121
N = 121

temp_number = []
i = M
while i >= M and i <= N:
    prime_number = True
    j = 2
    test_num = i
    if test_num > 1: # 1은 소수가 아니다.
        while j < test_num: 
            # 소수가 아닌것
            if test_num % j == 0:
                prime_number = False
                break
            j += 1
        # 소수가 인것
        if prime_number == True:
            temp_number.append(test_num)
    i += 1
if not temp_number:
    print('-1')
else:
    # print(temp_number)
    print(sum(temp_number))
    print(temp_number[0])
