import sys
repeat = 3

data = [int(sys.stdin.readline()) for i in range(repeat)]

mul = str(data[0] * data[1] * data[2])

num = ['0','1','2','3','4','5','6','7','8','9']

for i in range(10):
    print(mul.count(num[i]))

# print(mul.count('0'))
# print(mul.count('1'))
# print(mul.count('2'))
# print(mul.count('3'))
# print(mul.count('4'))
# print(mul.count('5'))
# print(mul.count('6'))
# print(mul.count('7'))
# print(mul.count('8'))
# print(mul.count('9'))