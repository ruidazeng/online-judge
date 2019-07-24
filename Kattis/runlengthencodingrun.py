descri, message = input().split()

if descri == 'E':
    counter = 1
    lastk = None
    for k in message:
        if k != lastk and lastk != None:
            print(lastk + str(counter), end = '')
            counter = 1
        elif k == lastk:
            counter += 1
        # Update state to hold value of lastest char
        lastk = k
    # Last char in sequence
    print(lastk + str(counter))
elif descri == 'D':
    for index, k in enumerate(message):
        if index % 2 == 0:
            for _ in range(int(message[index + 1])):
                print(k, end='')