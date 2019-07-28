alphabet = dict()

string = input()

for char in string:
    alphabet[char] = alphabet.get(char, 0) + 1

removed = -1
for char in alphabet:
    if alphabet[char] % 2 == 1:
        removed += 1 

if removed == -1: removed = 0
print(removed)