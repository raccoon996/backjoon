import sys
num = int(sys.stdin.readline()) 

data = [sys.stdin.readline() for i in range(num)]

data_count = [0 for i in range(num)]
data_count_temp = 0
for i in range(num):
    data_len = len(data[i])
    for j in range(data_len):
        if data[i][j] == 'O':
            data_count_temp += 1
        else:
            data_count_temp = 0
        data_count[i] = data_count[i] + data_count_temp
    print(data_count[i])
