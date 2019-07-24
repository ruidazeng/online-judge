while True:
    x, y = map(int, input().split())
    
    if x == 0 and y == 0:
        break
    
    botX, botY = 0, 0
    actX, actY = 0, 0
    n = int(input())
    for _ in range(n):
        move, distance = input().split()
        distance = int(distance)
        if move == 'u':
            actY += distance
            botY += distance
            if actY > y - 1:
                actY = y - 1
            elif actY < 0:
                actY = 0
        elif move == 'd':
            botY -= distance
            actY -= distance
            if actY > y - 1:
                actY = y - 1
            elif actY < 0:
                actY = 0
        elif move == 'r':
            botX += distance
            actX += distance
            if actX > x - 1:
                actX = x - 1
            elif actX < 0:
                actX = 0
        elif move == 'l':
            botX -= distance
            actX -= distance
            if actX > x - 1:
                actX = x - 1
            elif actX < 0:
                actX = 0
    
    print("Robot thinks", botX, botY)
    print("Actually at", actX, actY, '\n')