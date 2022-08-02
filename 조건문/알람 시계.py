H , M =input().split( )

H = int(H)
M = int(M)

M = M - 45

if M >= 0 and M <= 59 :
    print('{0} {1}'.format(H ,M))
else : 
    H = H - 1
    M = M + 60
    if H >= 0 and H <= 23 :
        print(f'{H} {M}')
    else :
        H = H + 24
        print(f'{H} {M}')
# if H >= 0 and H <= 23 :

# else :
#     print("error")