import sys
num = int(sys.stdin.readline()) 

data = list(map(int, sys.stdin.readline().split(' ')))

print(data)
min = min(data)
max = max(data)
print(f'{min} {max}')

