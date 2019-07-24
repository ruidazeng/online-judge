S = input()
level = len(S)
x = 0
y = 0

for i in range(level):
    if S[i] == '1' or S[i] == '3':
        x += 2**(level - i - 1)
    if S[i] == '2' or S[i] == '3':
        y += 2**(level - i - 1)

print(level, x, y)