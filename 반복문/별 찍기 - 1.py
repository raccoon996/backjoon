import sys

num = int(sys.stdin.readline())

for i in range(num):
    for j in range(i+1):
        print("*", end='')
    print(end='\n')