import copy
def copydic(**dict):
    global copy
    copie= dict.copy()
    return copie

def copyDic(**dic):
    new = {}
    for keys in dic.keys():
        new[keys]=dic[keys]
    return new

print(copydic(kolade=1))