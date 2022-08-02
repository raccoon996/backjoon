A , B = input().split( )
C = input()

A = int(A)
B = int(B)
C = int(C)

B = B + C

if B >= 0 and B <= 59 :
    print(f'{A} {B}')
else :
    A = A + (B//60)
    B = B - (B//60*60)
    if A >= 0 and A <= 23 :
        print(f'{A} {B}')
    else :
        A = A - (A//24*24)
        print(f'{A} {B}')
