n, b = input().split()
n = int(n) * 4
points = 0

for x in range(n):
    card = input()
    num = card[0]
    suit = card[1]
    if num == 'A':
        points += 11
    elif num == 'K':
        points += 4
    elif num == 'Q':
        points += 3
    elif num == 'T':
        points += 10
    # elif num == '8' or num == '9':
    #   points += 0
    elif suit == b:
        if num == 'J':
            points += 20
        elif num == '9':
            points += 14
    else:
        if num == 'J':
            points += 2
        # elif num == '9':
        #    points += 0

print(points)