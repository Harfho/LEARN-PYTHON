def adddic(dic1,dic2): #function onled too argd dic1 dic2
    new={} #new assign a empty dcct
    for keys in dic1.keys():# loop through the dic1 keys 
        new[keys]=dic1[keys] #and assign the value to new variable
    for keys in dic2.keys(): #loop through dic2 
        new[keys]=dic2[keys] #and asign the value to new variable 
    return new #return new

x = {'kolade':1}
y= {'rokkeb' :1}
print(adddic(x,y))