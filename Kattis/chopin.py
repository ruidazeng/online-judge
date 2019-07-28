import sys
unique = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
for index, line in enumerate(sys.stdin):
    note = line.split()
    if note[0] in unique:
        print("Case {0}: UNIQUE".format(index + 1))
    else:
        if note[0][1] == 'b':
            if note[0][0] == 'A':
                print("Case {0}: G# {1}".format(index + 1, note[1]))
            else:
                print("Case {0}: {1}# {2}".format(index + 1, unique[unique.index(note[0][0]) - 1], note[1]))
        elif note[0][1] == '#':
            if note[0][0] == 'G':
                print("Case {0}: Ab {1}".format(index + 1, note[1]))
            else:
                print("Case {0}: {1}b {2}".format(index + 1, unique[unique.index(note[0][0]) + 1], note[1]))