change = {'B':'8', 'G':'C', 'I':'1', 'O':'0', 'Q':'0', 'S':'5', 'U':'V', 'Y':'V', 'Z':'2'}
UCN = '0123456789ACDEFHJKLMNPRTVWX'

T = int(input())

for _ in range(T):
    k, finger = input().split()
    for char in finger:
        if char not in UCN:
            print(char)
            finger = finger.replace(char, change[char])
    #print(finger)
    d = -1
    answer = (2 * UCN.index(finger[d + 1])
    + 4 * UCN.index(finger[d + 2])
    + 5 * UCN.index(finger[d + 3])
    + 7 * UCN.index(finger[d + 4])
    + 8 * UCN.index(finger[d + 5])
    + 10 * UCN.index(finger[d + 6])
    + 11 * UCN.index(finger[d + 7])
    + 13 * UCN.index(finger[d + 8])) % 27
    if answer == UCN.index(finger[d + 9]):
        total = 0
        for j in range(8):
            total += UCN.index(finger[7 - j]) * (27 ** j)
        print(k, total)
    else:
        print(k, "Invalid")