import sys
T = int(sys.stdin.readline())

data = [list(map(int, sys.stdin.readline().split(' '))) for i in range(T)]

# room_num = []
room_num = 0
for i in range(T):
    H = data[i][0]
    W = data[i][1]
    N = data[i][2]
    # 층
    YY = (N - 1) % H + 1
    # 호수
    XX = ((N - 1) // H) + 1
    # room_num.append(YY*100 + XX)
    room_num = YY*100 + XX
    print(room_num)

# 생각해봐야 하는 상황
# 1호를 선호
# 낮은 층을 선호