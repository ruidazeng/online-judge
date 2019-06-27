n = int(input())

for i in range(n):
    lineOne = input()
    lineTwo = input()
    print(lineOne)
    print(lineTwo)
    for j in range(len(lineOne)):
        if lineOne[j] != lineTwo[j]:
            print('*', end = '')
        else:
            print('.', end = '')
    print("\n")