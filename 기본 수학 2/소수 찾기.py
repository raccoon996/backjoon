import sys
N = int(sys.stdin.readline())

data_num = list(map(int, sys.stdin.readline().split(' ')))

prime_number_count = 0
for i in range(N):
    j = 2
    test_num = data_num[i]
    if test_num > 1:
        while j < test_num:
            if test_num % j == 0:
                data_num[i] = 0
                N -= 1
                break
            j += 1
    else:
        N -= 1
        data_num[i] = 0
# prime_number_count = N - str(data_num).count('0')
print(N)