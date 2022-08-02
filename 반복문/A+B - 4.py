import sys
AB_input = sys.stdin.readline

resultList = []
while True:
    try : 
        A, B = map(int,AB_input().split())
        if A < 10 and B < 10:
            # print(f'{A} + {B} = {A+B}')
            # print(f'{A+B}')
            resultList.append(A+B)            
        else:
            print('error')
    except :
        break

print(*resultList, sep = '\n')

# 반복문 사용
# rows = [[r * 10 + c for c in range(10)] for r in range(10)]
