line = input()
vowel = 'aeiou'
decoded = ''
i = 0

while i < len(line):
    decoded += line[i]
    if line[i] in vowel:
        i += 2
    i += 1

print(decoded)