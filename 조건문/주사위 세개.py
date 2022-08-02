A , B , C = map(int, input().split( ))

if A == B == C:
    money = 10000 + A * 1000
elif A == B or A == C :
    money = 1000 + A * 100
elif B == C :
    money = 1000 + B * 100
else : 
    if A > B and A > C:
        money = A * 100
    elif B > A and B > C:
        money = B * 100
    elif C > A and C > B:
        money = C * 100

print(money)