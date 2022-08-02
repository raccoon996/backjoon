def solve(number):
    a = number
    if a > 9999:
        return
    else:
        temp_sum = a
        while a != 0:
            temp_sum = temp_sum + (a % 10)
            a = a // 10
    return  temp_sum

num_count = 10000
check = [0 for i in range(num_count+1)]
for i in range(num_count):
    n = solve(i)
    if n <= num_count:
        check[n] = 1
# slef_num = list(filter(lambda n: n == 0 , check))

for i in range(num_count):
    if check[i] == 0:
        print(f'{i}')