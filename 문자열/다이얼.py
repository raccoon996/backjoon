import sys
word = list(sys.stdin.readline())

time = {3:["A","B","C"], 4:["D","E","F"], 5:["G","H","I"],6:["J","K","L"],
        7:["M","N","O"], 8:["P","Q","R","S"],9:["T","U","V"], 10:["W","X","Y","Z"]}

dir = 0
for i in word:
    for k, v in time.items():
        if i in v :
            dir += k

print(dir)

# time = 0
# for i in range(len(word)):
#     for j in range(26):
#         if word[i] == chr(j+65):
#             time = (j//3) + 3 + time
#             if j == 25:
#                 time -= 1
# print(time)


# word = input().upper()

# time = {3:["A","B","C"], 4:["D","E","F"], 5:["G","H","I"],6:["J","K","L"],
#         7:["M","N","O"], 8:["P","Q","R","S"],9:["T","U","V"], 10:["W","X","Y","Z"]}

# dir = 0
# for i in word:
#     for k, v in time.items():
#         if i in v :
#             dir += k

# print(dir)

# 딕셔너리
# items는 딕셔너리
# values
# clear
# get
# keys
# 예시 {Key1:Value1, Key2:Value2, Key3:Value3, ...}