# import sys

# A = list(range(10))
# B = list(range(10))
# i = 0
# while True:
#     A[i], B[i] = map(int,sys.stdin.readline().split())
#     if A[i] == 0 and B[i] == 0:
#         break
#     else:
#         i += 1

# for j in range(i):
#     print(A[j]+B[j])


import sys

# A = list(range(10))
# B = list(range(10))
while True:
    A, B= map(int,sys.stdin.readline().split())
    if A == 0 and B == 0:
        break
    else:
        print(A+B)
