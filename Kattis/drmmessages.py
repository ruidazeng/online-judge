from string import ascii_uppercase as upABC

LET = 26

def split_list(s):
    half = len(s)//2
    return s[:half], s[half:]
    
def rotValue(s):
    value = 0
    for x in s:
        value += upABC.index(x)
    return value

def rotation(s, n):
    return ''.join(upABC[(upABC.index(x) + n) % LET] for x in s)

def merge(s1, s2):
    return ''.join(rotation(s1[i], upABC.index(s2[i])) for i in range(len(s2)))
    
enDrm = input()
firstDrm, secondDrm = split_list(enDrm)
firstDrm = rotation(firstDrm, rotValue(firstDrm))
secondDrm = rotation(secondDrm, rotValue(secondDrm))
deDrm = merge(firstDrm, secondDrm)
print(deDrm)