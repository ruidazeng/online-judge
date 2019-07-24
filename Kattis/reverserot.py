SCHEME = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    message = input()
    if message == '0':
        break
    n, message = message.split()
    print("".join(SCHEME[(SCHEME.index(char) + int(n)) % len(SCHEME)]
    for char in message[::-1]))