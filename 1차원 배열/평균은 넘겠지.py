import sys
C = int(sys.stdin.readline()) 

TEST_CASE = [list(map(int, sys.stdin.readline().split(' ')))  for i in range(C)]

for i in range(C):
    student_B = 0
    student_num = int(TEST_CASE[i][0])
    filter_st = list(filter(lambda n: n > ((sum(TEST_CASE[i])-student_num) / student_num), TEST_CASE[i]))
    student_B = len(filter_st)
    print(student_B)
    answer2 = round(student_B/student_num*100)
    print('%.3f%%' %answer2)

# for i in range(C):
#     student_B = 0
#     student_num = int(TEST_CASE[i][0])
#     test_AVG = (sum(TEST_CASE[i])-student_num) / student_num
#     for j in range(len(TEST_CASE[i])):
#         if TEST_CASE[i][j] > test_AVG:
#             student_B += 1 
#     answer1 = round(student_B/student_num*100,3)
#     print('%.3f%%' %answer1)


