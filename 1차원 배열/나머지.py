import sys
repeat = 10
count = 0

data = [int(sys.stdin.readline()) for i in range(repeat)]

dataappend = []
for i in range(repeat):
    data[i] = data[i]%42
    dataappend.append(data[i]%42)

for i in range(42):
    if i in data:
        count += 1
    else:
        pass
print(count)


# count_temp = [0]*repeat
# count = 0
# for i in range(repeat):
#     for j in range(i,repeat):
#         if data[j] != -1:
#             if data[i] == data[j]:
#                 data[j] =  -1
#                 count_temp[i] += 1 
# print(count_temp)



