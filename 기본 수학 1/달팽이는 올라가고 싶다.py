import sys
A, B, V = map(int, sys.stdin.readline().split(' '))

day = ((V - B - 1)//(A - B)+1) 
print(f'{day}')

# 생각해봐야 하는 상황
# 1. A > V : 하루면 끝남
# 2. A = V : 하루면 끝남
# 3. A < V : 이틀 이상이 걸림

# 3번 조건에 충족하지 못함
# day = ((V - B)//(A - B)+1) 


# 1번 조건에 충족하지 못함
# day = ((V - A)//(A - B)) 
# decimal_point = day - ((V - A)/(A - B))
# day += 1 # 마지막날 올라 가는 것
# if decimal_point > 0:
#     day += 1
# print(f'{day}')



# 시간이 많이 걸리는 문제가 있음
# day = 0
# leftover = V
# while leftover > 0:
#     day += 1
#     leftover -= A
#     if leftover <= 0:
#         print(f'{day}')
#         break
#     leftover += B
