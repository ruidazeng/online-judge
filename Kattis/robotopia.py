T = int(input())

for _ in range(T):
    l1, a1, l2, a2, lt, at = map(int, input().split())
    x = 1
    solution = []
    while l1 * x < lt:
        y = int((lt - l1 * x)/l2)
        if l1 * x + l2 * y == lt and a1 * x + a2 * y == at:
            solution.append([int(x), int(y)])
        x += 1

    if len(solution) != 1:
        print('?')
    else:
        print(*solution[0])