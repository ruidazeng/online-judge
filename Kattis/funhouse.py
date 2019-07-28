def move(x_cord, y_cord, dir):
    if dir == 'N':
        x_cord -= 1
    elif dir == 'S':
        x_cord += 1
    elif dir == 'E':
        y_cord += 1
    elif dir == 'W':
        y_cord -= 1
    return (x_cord, y_cord)


index = 0

while True:
    w, l = map(int, input().split())
    if w == 0 and l == 0: break

    # actual processing
    index += 1
    maze = [[c for c in input()] for _ in range(l)]
    # print(maze)
    for i in range(l):
        for j in range(w):
            if maze[i][j] == '*':
                # (x, y) coordinates
                x_cord = i
                y_cord = j

    # print(x_cord, y_cord)
    if x_cord == 0 and y_cord != 0:
        dir = 'S'
    elif x_cord != 0 and y_cord == 0:
        dir = 'E'
    elif y_cord == w - 1:
        dir = 'W'
    elif x_cord == l - 1:
        dir = 'N'
    
    # looping
    while True:
        # print(x, y, dir)
        temp = move(x_cord, y_cord, dir)
        x_cord = temp[0]
        y_cord = temp[1]
        if maze[x_cord][y_cord] == '.':
            continue
        elif maze[x_cord][y_cord] == '/':
            if dir == 'W':
                dir = 'S'
            elif dir == 'S':
                dir = 'W'
            elif dir == 'E':
                dir = 'N'
            elif dir == 'N':
                dir = 'E'
        elif maze[x_cord][y_cord] == '\\':
            if dir == 'W':
                dir = 'N'
            elif dir == 'N':
                dir = 'W'
            elif dir == 'E':
                dir = 'S'
            elif dir == 'S':
                dir = 'E'
        elif maze[x_cord][y_cord] == 'x':
            maze[x_cord][y_cord] = '&'
            print('HOUSE', index)
            for i in range(l):
                for j in range(w):
                    print(maze[i][j], end = '')
                print()
            break