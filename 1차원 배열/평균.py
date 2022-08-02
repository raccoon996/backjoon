import sys
num = int(sys.stdin.readline()) 

data = list(map(int, sys.stdin.readline().split(' ')))
data_sum = sum(data)
max_avg = (data_sum/num)/max(data)*100

print(f'{max_avg}')