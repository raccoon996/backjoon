import sys
T = int(sys.stdin.readline())

data = [int(sys.stdin.readline()) for i in range(T*2)]


# for data_num in range(T):
#     k.append
for T_num in range(T):
    Apartment = [[0 for row in range(data[T_num*2]+1)]for col in range(14)]
    for k in range(data[T_num*2]+1):
        Apartment[0][k] = 1
        for n in range(data[T_num*2+1]):
            if k == 0:
                Apartment[n][k] = n+1
            elif n != 0:
                Apartment[n][k] = Apartment[n-1][k] + Apartment[n][k-1]
    print(Apartment[n][k])

# Apartment = [[0 for row in range(data[0]+1)]for col in range(14)]
# for k in range(data[0]+1):
#     Apartment[k][0] = 1
#     for n in range(data[1]):
#         if k == 0:
#             Apartment[k][n] = n+1
#         elif n != 0:
#             Apartment[k][n] = Apartment[k-1][n] + Apartment[k][n-1]
# print(Apartment[k][n])