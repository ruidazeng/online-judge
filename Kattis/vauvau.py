A, B, C, D = map(int, input().split())
P, M, G = map(int, input().split())

for time in [P, M, G]:
    attack = 0
    dog1 = time%(A+B)
    dog2 = time%(C+D)
    if dog1 != 0 and dog1 <= A:
        attack += 1
    if dog2 != 0 and dog2 <= C:
        attack += 1
    
    if attack == 0:
        print('none')
    elif attack == 1:
        print('one')
    elif attack == 2:
        print('both')