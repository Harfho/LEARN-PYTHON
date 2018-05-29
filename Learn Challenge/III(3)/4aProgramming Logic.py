L = [1, 2, 4, 8, 16, 32, 64]
X = 5
found = True
i = 0
while found:
    if i < len(L):
        if 2**5==L[i]:
            print('Found at index',i)
            found = False
    else:
            print(i,'Not found')
    i +=1
input()