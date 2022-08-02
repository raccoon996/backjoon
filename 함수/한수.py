def arithmetic(number):
    arithmetic_count = 0
    for i in range(number+1):
        if 0 < i < 10:
            arithmetic_count += 1
        elif 10 <= i < 100:
            arithmetic_count += 1
        elif 100 <= i < 1000:
            each_number = [0 for j in range(len(str(i)))]
            digit = 0
            a = i
            while a != 0:
                each_number[digit] = (a % 10)
                digit += 1
                a = a // 10
            difference_1 = each_number[2] - each_number[1]
            difference_2 = each_number[1] - each_number[0]
            if difference_1 == difference_2:
                arithmetic_count += 1
    return arithmetic_count

import sys
N = int(sys.stdin.readline()) 
arithmetic_count = arithmetic(N)
print(f'{arithmetic_count}')