sciCard = input()
t, c, g = 0, 0, 0

for x in sciCard:
    if x == "T":
        t += 1 
    elif x == 'C':
        c += 1 
    elif x == 'G':
        g += 1 
    
points = t ** 2 + c ** 2 + g ** 2 + 7 * min(t, c, g)
print(points)