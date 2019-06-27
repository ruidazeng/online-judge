cipher = input()

cipher = list(cipher)
days = 0

for i in range(len(cipher)):
    if not ((cipher[i] == 'P' and i % 3 == 0) or
    (cipher[i] == 'E' and i % 3 == 1) or
    (cipher[i] == 'R' and i % 3 == 2)):
        days += 1

print(days)