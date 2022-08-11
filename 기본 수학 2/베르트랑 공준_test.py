def prime_list(n):
    sieve = [True] * n 
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

while 1:
    n=int(input())
    if n == 0: break
    li = prime_list(2*n+1)
    print(len([i for i in li if i>n]))


# 시간초과
# import sys

# def is_prime(n) :
#     if n == 2 :
#         return True

#     if n % 2 == 0 :
#         return False
    
#     for i in range(2, int(n ** 0.5) + 1) :
#         if n % i == 0 :
#             return False

#     return True

# while True:
#     n = int(sys.stdin.readline())

#     if n == 0 :
#         break

#     prime_cnt = 0

#     for i in range(n+1, (2*n)+1) :
#         if is_prime(i) :
#             prime_cnt += 1

#     print(prime_cnt)