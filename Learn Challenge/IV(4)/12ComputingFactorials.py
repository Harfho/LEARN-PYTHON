def fact0(N):
    if N==1:
        return N
    else:
        return( N * fact0(N-1))

def fact1(N):
    l=[]
    for x in range(1,N+1):
        l.append(x)
    su=0+1
    for y in l[:]:
        su *= y
    return su

print(fact1(0))
#print(fact0(12345))