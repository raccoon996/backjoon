import sys
N = int(sys.stdin.readline())

temp_num = N
result = []
while temp_num > 1:
    i = 2
    while True:
        if temp_num // i == temp_num / i:
            temp_num = temp_num // i
            result.append(i)
            print(i)
            break
        i += 1