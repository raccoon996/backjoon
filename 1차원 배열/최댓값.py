import sys
repeat = 9

data = [int(sys.stdin.readline())  for i in range(repeat)]
# print(data)

max = max(data)
print(f'{max}')
print(data.index(max)+1)