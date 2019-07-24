abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

message = input()
old_key = input()

result = ''
new_keyz = ''
for char, kee in zip(message, old_key):
    num = abc.index(char) - abc.index(kee)
    new_keyz += abc[num]

# last char is the new_key
result += new_keyz

for i, char in zip(range(0, len(message)), message[len(old_key):]):
    num = abc.index(char) - abc.index(result[i])
    result += abc[num]
print(result)