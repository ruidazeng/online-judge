ABC = ' abcdefghijklmnopqrstuvwxyz'
T = int(input())
for _ in range(T):
    string = input()
    purpose = string[0]
    actual = string[2:]
    if purpose == 'e':
        symbol = []
        for char in actual:
            symbol.append(ABC.index(char))
        for index in range(1, len(symbol)):
            symbol[index] += symbol[index - 1]
        for index in range(len(symbol)):
            symbol[index] %= 27
        for index in symbol:
            print(ABC[index], end = '')
        print()
    elif purpose == 'd':
        symbol = []
        for char in actual:
            symbol.append(ABC.index(char))
        # adjust for modulus
        for index in range(1, len(symbol)):
            while symbol[index] < symbol[index - 1]:
                symbol[index] += 27
        for index in range(len(symbol)-1, 0, -1):
            symbol[index] -= symbol[index - 1]
        for index in symbol:
            print(ABC[index], end = '')
        print()