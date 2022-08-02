import sys
X = int(sys.stdin.readline())

N = 0
N_sum = 0
old_N_sum = 0
while True:
    N += 1
    N_sum += N
    if old_N_sum < X and X <= N_sum:
        numerator = X - old_N_sum
        denominator = N - numerator + 1
        print(f'{numerator}/{denominator}')
        break
    old_N_sum = N_sum

NN=1