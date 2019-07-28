goal_x, goal_y = map(int, input().split())

possible = ['N', 'E', 'S', 'W']
def movement(lst):
    face = 'N'
    x, y = 0, 0
    for move in lst:
        if move == 'Forward':
            if face == 'N':
                y += 1
            elif face == 'S':
                y -= 1
            elif face == 'W':
                x -= 1
            if face == 'E':
                x += 1
        elif move == 'Left':
            face = possible[(possible.index(face) - 1) % 4]
        elif move == 'Right':
            face = possible[(possible.index(face) + 1) % 4]
    if x == goal_x and y == goal_y:
        return True
    else:
        return False

T = int(input())
instructions = [input() for _ in range(T)]
for index, ins in enumerate(instructions):
    if ins == 'Forward':
        new_list = [x for x in instructions]
        new_list[index] = 'Right'
        if movement(new_list):
            print(index + 1, 'Right')
            break
        new_list[index] = 'Left'
        if movement(new_list):
            print(index + 1, 'Left')
            break
    elif ins == 'Left':
        new_list = [x for x in instructions]
        new_list[index] = 'Forward'
        if movement(new_list):
            print(index + 1, 'Forward')
            break
        new_list[index] = 'Right'
        if movement(new_list):
            print(index + 1, 'Right')
            break
    elif ins == 'Right':
        new_list = [x for x in instructions]
        new_list[index] = 'Forward'
        if movement(new_list):
            print(index + 1, 'Forward')
            break
        new_list[index] = 'Left'
        if movement(new_list):
            print(index + 1, 'Left')
            break