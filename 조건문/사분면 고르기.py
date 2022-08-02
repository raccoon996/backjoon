X = input()
Y = input()

X = int(X)
Y = int(Y)

if X > 0 :
    if Y > 0 :
        print("1")
    elif Y < 0 :
        print("4")
    else :
        print("error")    
elif X < 0 :
    if Y > 0 :
        print("2")
    elif Y < 0 :
        print("3")
    else :
        print("error")   
else :
    print("error")