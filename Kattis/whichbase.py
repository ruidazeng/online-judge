def octal(num):
    test = str(num)[::-1]
    octal = 0
    if '9' in test or '8' in test:
        return 0
    else:
        for index, char in enumerate(test):
            octal += int(char) * (8 ** index)
        return octal
            

def decimal(num):
    return num

def hexa(num):
    hexa = 0
    test = str(num)[::-1]
    for index, char in enumerate(test):
        hexa += int(char) * (16 ** index)
    return hexa

T = int(input())
for _ in range(T):
    k, n = map(int, input().split())
    print(k, octal(n), decimal(n), hexa(n))