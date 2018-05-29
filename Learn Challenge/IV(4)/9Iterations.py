li=[2,4,9,16,25]

li1=[]
for i in li:   #using for loop
    li1.append(i*2)
print(li1)

print([li2*2 for li2 in li]) #using list comphension

print(list(map(lambda li3:li3*2,li))) #using map

print(list((li2*2 for li2 in li)))#using generator
