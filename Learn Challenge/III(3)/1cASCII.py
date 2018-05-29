s = 'kolade'
addup =[]
for n in s:
    addup.append(ord(n))

print(addup) #MANUAL LOOPING

print(list(map(ord,s))) #MAPPING

print([ord(c) for c in s]) #USING LIST COMPREHENSION

input()