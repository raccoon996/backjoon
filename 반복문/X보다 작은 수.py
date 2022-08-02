import sys

N , X = map(int,sys.stdin.readline().split())

data = sys.stdin.readline().split()

for i in range(N):
    if int(data[i]) < X:
        print(data[i], end=' ')
