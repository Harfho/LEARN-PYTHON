#using for loop
def countdown(x): 
    recur=[]
    for x in range(x+1):
        recur.append(x)
    for y in recur[:]:
        print(recur.pop(),end=' ')
        
#using generator     
##def countdown2(x):
##    for x in range(x+1):
##        yield x
##li=[]
##for x in countdown2(4):
##    li.append(x)
##li.sort(reverse=True)
##for i in li:
##    print(i)
    
countdown(4)