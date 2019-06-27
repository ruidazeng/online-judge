moves = input()

state = 1 # leftmost

for x in moves:
    if x == 'A':
        if state == 1:
            state = 2
        elif state == 2:
            state = 1
    elif x == 'B':
        if state == 2:
            state = 3
        elif state == 3:
            state = 2
    elif x == 'C':
        if state == 1:
            state = 3
        elif state == 3:
            state = 1 

print(state)