line = input()

white = line.count('_') / len(line)
print(format(white, '.16f'))

lower = len([x for x in line if x.islower()]) / len(line)
print(format(lower, '.16f'))

upper = len([x for x in line if x.isupper()]) / len(line)
print(format(upper, '.16f'))

symbols = 1 - (white + lower + upper)
print(format(symbols, '.16f'))