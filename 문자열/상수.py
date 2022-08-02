import sys
S = list(map(int, sys.stdin.readline().split()))
A=[]
for i in range(2):
    hundred = (S[i]//100)
    ten =  ((S[i]-hundred*100)//10)
    one = (S[i]-hundred*100-ten*10)
    A.append(one*100+ten*10+hundred)
max_A = max(A)
print(max_A)