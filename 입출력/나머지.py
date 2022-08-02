A, B, C=input().split( )
A = int(A)
B = int(B)
C = int(C)

ans1 = (A + B)%C
ans2 = ((A%C) + (B%C))%C
ans3 = (A * B)%C
ans4 = ((A%C) * (B%C))%C

print(ans1)
print(ans2)
print(ans3)
print(ans4)