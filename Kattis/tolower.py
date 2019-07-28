P, T = map(int, input().split())
solved = 0

for _ in range(P):
    flag = True
    for _ in range(T):
        test1 = input().strip()
        test = test1[0].lower() + test1[1:]
        if test == test1.lower():
            continue
        else:
            flag = False
    if flag:
        solved += 1
print(solved)