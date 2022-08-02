import sys
repeat = 3

data = [int(sys.stdin.readline()) for i in range(repeat)]

mul = data[0] * data[1] * data[2]
print(mul)
mul = str(mul)

# count = [0 for i in range(9)]
# count = []
# for i in range(9):
#     mui_temp = mul // (10**(9-i))
#     print(mui_temp)
#     # count[9-i] = mui_temp
#     count.append(str(mui_temp))
#     mul = mul - (mui_temp * (10**(9-i)))

print(mul.count('0'))
print(mul.count('1'))
print(mul.count('2'))
print(mul.count('3'))
print(mul.count('4'))
print(mul.count('5'))
print(mul.count('6'))
print(mul.count('7'))
print(mul.count('8'))
print(mul.count('9'))