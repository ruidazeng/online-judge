T = int(input())
for _ in range(T):
    sound = input().split()
    while True:
        case = input()
        if case == 'what does the fox say?': break
        case = case.split()
        if case[2] in sound:
            while case[2] in sound: sound.remove(case[2])
    print(*sound)