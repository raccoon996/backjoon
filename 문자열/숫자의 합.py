import sys
N = sys.stdin.readline()
number = int(sys.stdin.readline())
temp_sum = 0
while number != 0:
    temp_sum = temp_sum + (number % 10)
    number = number // 10
print(f'{temp_sum}')