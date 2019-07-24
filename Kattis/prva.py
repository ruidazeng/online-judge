# Object-oriented Programming in Python
# Made some edits to optimize and simplified the codes

class Board:
    def __init__(self, R, C):
        self.R = R
        self.C = C
        # self.grid[row][col]
        self.grid = [['#']*C for _ in range(R)]

    def add_char(self, row, col, c):
        self.grid[row][col] = c

    # Reads all the words from the board
    def get_words(self):
        all_words = []
        
        # Iterate through rows
        for r in range(self.R):
            word = ''
            for c in range(self.C):
                char = self.grid[r][c]
                if char == '#':
                    if len(word) >= 2:
                        all_words.append(word)
                    word = ''
                else:
                    word += char
                    
            # This here is crucial (in case the line has no #)
            if len(word) >= 2:
                all_words.append(word)

        # Iterate through columns
        for c in range(self.C):
            word = ''
            for r in range(self.R):
                char = self.grid[r][c]
                if char == '#':
                    if len(word) >= 2:
                        all_words.append(word)
                    word = ''
                else:
                    word += char
            
            # This here is crucial (in case the line has no #)
            if len(word) >= 2:
                all_words.append(word)
                
        return all_words
                


R, C = map(int, input().split())
myBoard = Board(R, C)
for r in range(R):
    l = input()
    for c in range(C):
        if l[c] == '#':
            continue
        myBoard.add_char(r, c, l[c])

# min returns lexicographically shortest word in the lists of words
print(min(myBoard.get_words()))