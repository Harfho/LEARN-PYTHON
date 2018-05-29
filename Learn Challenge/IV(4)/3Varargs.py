##def adder1(*args):
##    print('adder1',end=' ')
##    if type(args[0])==int:
##        sum = 0
##    else:
##        sum=args[0][:0]
##    for arg in args:
##        sum =sum+arg
##    return sum
##
##def adder2(*args):
##    print('adder2',end=' ')
##    sum =args [0 ] ##Init to arg1
##    for next in args [1:]:
##        sum +=next #Add items 2..N
##    return sum

def adder3(*args):
    print('adder3',end=' ')
    if type(args[0])==int:
        for arg in args:
            sum = 0+arg
        return sum
    else:
        sume = args[0][:0]
        for arg in args:
            sume =sume + arg
        return sume
    
##print(adder1(1,2,3))
##print(adder1([1,2],[3,4]))
##print(adder2(1,2,3))
##print(adder2([1,2],[3,4]))
##print(adder1('kolade','rokeeb'))
##print(adder2('kolade','rokeeb'))

print(adder3(1,2,3))
print(adder3([1,2],[3,4]))
print(adder3('kolade','rokeeb'))

