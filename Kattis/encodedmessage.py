import math

t = int(input())

for _ in range(t):
    enMsg = input()
    size = int(math.sqrt(len(enMsg)))
    
    # "None" serves as a placeholder
    enGrid = [[None] * size for _ in range(size)]
    for i, val in enumerate(enMsg):
        row = i // size
        col = i % size
        enGrid[col][row] = val

    deGrid = ''.join([''.join(col) for col in enGrid[::-1]])
    print(deGrid)