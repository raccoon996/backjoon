A=input()
B=input()

A = int(A)
B = int(B)

B000 = B//100
B00  = (B-(B000*100))//10
B0   = B-(B000*100)-(B00*10)

ans3 = A*B0
ans4 = A*B00
ans5 = A*B000

ans6 = A*B
print(ans3)
print(ans4)
print(ans5)
print(ans6)