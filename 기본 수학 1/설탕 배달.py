import sys
N = int(sys.stdin.readline())

if N == 4 or N == 7:
    print('-1')
else:
    beg_count = (N // 5) - ((N % 5) % 3) + (((N % 5) % 3) * 5 + (N % 5))//3
    # N//5 : 5kg 봉지 개수
    # (N % 5) % 3 : 3kg 봉지에 맞추기 위한 5kg 봉지 개수
    # ((N % 5) % 3) * 5 : 5kg 봉지 개수 * 5 = 깐 kg
    # (N % 5) : 나머지 kg (1 ~ 4)
    print(beg_count)



    # Remain = N % 5
    # if Remain == 1:
    #     beg_count = (N // 5) - 1 + 2
    # elif Remain == 2:
    #     beg_count = (N // 5) - 2 + 4
    # elif Remain == 3:
    #     beg_count = (N // 5) + 1
    # elif Remain == 4:
    #     beg_count = (N // 5) - 1 + 3
    # elif Remain == 5:
    #     beg_count = (N // 5)
    # else:
    #     beg_count = -1    