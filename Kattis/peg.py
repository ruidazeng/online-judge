from array import *
matrix = [[None for _ in range(7)] for _ in range(7)]

def top(matrix, i, j):
    if matrix[i - 1][j] == 'o' and matrix[i - 2][j] == '.':
        return 1 
    else:
        return 0

def down(matrix, i, j):
    if matrix[i + 1][j] == 'o' and matrix[i + 2][j] == '.':
        return 1 
    else:
        return 0

def left(matrix, i, j):
    if matrix[i][j - 1] == 'o' and matrix[i][j - 2] == '.':
        return 1 
    else:
        return 0
        
def right(matrix, i, j):
    if matrix[i][j + 1] == 'o' and matrix[i][j + 2] == '.':
        return 1 
    else:
        return 0
# parse inputs
for i in range(2):
    string = 'xx' + input().strip() + 'xx'
    for j, char in enumerate(string):
        matrix[i][j] = char

# parse inputs
for i in range(2, 5):
    string = input().strip()
    for j, char in enumerate(string):
        matrix[i][j] = char

# parse inputs
for i in range(5, 7):
    string = 'xx' + input().strip() + 'xx'
    for j, char in enumerate(string):
        matrix[i][j] = char

count = 0
for i in range(7):
    for j in range(7):
        t = d = l = r = True
        tmp = matrix[i][j]
        if tmp == 'x' or tmp == '.': continue
        # if at left, don't check left
        if j == 0 or j == 1:
            l = False
        # if at right, don't check right
        if j == 6 or j == 5:
            r = False
        # if at top, don't check top
        if i == 0 or i == 1:
            t = False
        # if at bottom, don't check down
        if i == 6 or i == 5:
            d = False
        # else check left, right, up, down
        if (t):
            count += top(matrix, i, j)
        if d:
            count += down(matrix, i, j)
        if r:
            count += right(matrix, i, j)
        if l:
            count += left(matrix, i, j)

print(count)