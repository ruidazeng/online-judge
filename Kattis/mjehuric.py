def bubblesort(vals):
    changed = True
    while changed:
        changed = False
        for i in range(len(vals) - 1):
            if vals[i] > vals[i + 1]:
                changed = True
                vals[i], vals[i + 1] = vals[i + 1], vals[i]
                # Yield gives the "state"
                yield vals

vals = [int(x) for x in input().split()]
for state in bubblesort(vals):
    print(*state)