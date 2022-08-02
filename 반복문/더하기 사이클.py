# 기간초과
# import sys
# N_input = sys.stdin.readline

# N = int(N_input())
# N_count = 0

# while True:
#     try:
#         if N_count == 0:
#             # 처음 들어왔을 때
#             N_ten = N // 10
#             N_one = N - (N_ten*10)
            
#             N_ten_Next = N_one # 앞 숫자의 일의 자리
#             N_one_Next = (N_ten + N_one) - ((N_ten + N_one)//10) #  10의 자리와 1의 자리 합의 1의 자리
#             N_count += 1
#         else:
#             N_ten = N_ten_Next
#             N_one = N_one_Next
#             if (N_ten*10 + N_one) == N :
#                 print(N_count)
#                 break
#             else:
#                 N_ten_Next = N_one
#                 N_one_Next = (N_ten + N_one) - ((N_ten + N_one)//10) * 10
#                 N_count += 1
#     except:
#         break
###############################################################################################################
# import sys
# N_input = sys.stdin.readline

# N = int(N_input())
# N_count = 1
# N_ten = N // 10
# N_one = N - (N_ten*10)
# N_ten_Next = N_one 
# N_one_Next = (N_ten + N_one) - ((N_ten + N_one)//10) * 10 

# while True:
#     N_ten = N_ten_Next
#     N_one = N_one_Next
#     if (N_ten*10 + N_one) == N :
#         print(N_count)
#         break
#     else:
#         N_ten_Next = N_one
#         N_one_Next = (N_ten + N_one) - ((N_ten + N_one)//10) * 10
#         N_count += 1
###############################################################################################################
# import sys
# N_input = sys.stdin.readline
# N_count = 0

# N = int(input())

# N_ten = N // 10
# N_one = N % 10 
# N_ten_Next = N_one
# N_one_Next = (N_ten + N_one) % 10
# N_Next = N_ten_Next*10 + N_one_Next
# N_count += 1

# while N != N_Next :
#     N_ten = N_ten_Next
#     N_one = N_one_Next 
#     N_ten_Next = N_one
#     N_one_Next = (N_ten + N_one) % 10
#     N_Next = N_ten_Next*10 + N_one_Next
#     N_count += 1
# print(N_count)
###############################################################################################################

# append 함수 이용  # 리스트가 하나의 객체로 추가되었음
N = int(input())

if 0 <= N < 10:
    N = '0'+ str(N)

N = list(str(N))
N_count = 0

while True:
    N.append(str((int(N[N_count])+int(N[N_count+1]))%10)) # 리스트가 하나의 객체로 추가되었음
    N_count += 1
    if N[0]+N[1] == N[N_count]+N[N_count+1]:
        print(N_count)
        break