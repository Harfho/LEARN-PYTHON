def f1(a, b): print(a, b) # Normal args
def f2(a, *b): print(a, b) # Positional varargs
def f3(a, **b): print(a, b) # Keyword varargs
def f4(a, *b, **c):
##    new=[]
##    for dic in c:
##        new.append(c[dic])
##    su=[]
##    for i in b:
##        su.append(i)
    print(a,b,c)
def f5(a, b=2, c=3): print(a, b, c) # Defaults
def f6(a, b=2, *c): print(a, b, c) # Defaults and positional varargs

