night_move = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

def check_valid(board, x, y):
    # Check if there are knights on positions where the knight can reach
    for a, b in [(x + a, y + b) for a, b in night_move]:
        if 0 <= a < 5 and 0 <= b < 5 and board[a][b] == 'k':
            return False
    return True


board = [input() for _ in range(5)]
knt = 0
find = False
# Go through the grid until all 9 knights are "valid"
for i in range(5):
    for j in range(5):
        if board[i][j] != 'k':
            continue
        knt += 1
        if not check_valid(board, i, j):
            find = True
    if find:
        break
        
print("valid" if knt == 9 else "invalid")