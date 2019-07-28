numbs = [int(x) for x in input().split()]
numbs = sorted(numbs)
A, B, C = numbs

lets = [char for char in input()]

for char in lets:
    print(eval(char), end = ' ')