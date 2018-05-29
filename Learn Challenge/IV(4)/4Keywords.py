#WORK FOR ANY DATA TYPES
def adder1(**args):
    print('adder1',end=' ')
    tot=[]
    for keys in args:
        tot.append(args[keys])
    
    if type(tot[0] ) == type(''):
        su=''
        for li in tot[:]:
            store=li
            su =su + store
        return su
    
    elif type(tot[0])== type([]):
        su=[]
        for li in tot[:]:
            store=li
            su =su + store
        return su
    
    elif type(tot[0])==type(0):
        stor=sum(tot)
        return stor
    else:
        return tot

#Not work for all data type
def adder2(**args):#Same,but convert to list of values
    print('adder2',end =' ')
    args =list(args.values())#list needed to index in 3.X!
    tot =args [0 ]
    for arg in args [1:]:
        tot +=arg
    return tot

#Cant work for all data type
def adder3(*args):#Sum any number of positional args
    tot =args [0 ]
    for arg in args [1:]:
        tot +=arg
    return tot
def adder4(**args):#Sum any number of keyword args
    argskeys =list(args.keys())#list needed in 3.X!
    tot =args [argskeys [0 ]]
    for key in argskeys [1:]:
        tot +=args [key ]
    return tot

print(adder2( ko= (1,2,3) ) )