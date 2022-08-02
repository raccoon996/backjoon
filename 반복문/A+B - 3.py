repeat = int(input())

A = list(range(repeat))
B = list(range(repeat))

for i in range(repeat):
    A[i], B[i] = map(int,input().split())

for i in range(repeat): 
    print(A[i]+B[i])
