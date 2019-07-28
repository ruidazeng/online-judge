P = []
K = []
H = []
T = []

line = input()

# a little hardcoding
cards = [line[i:i+3] for i in range(0, len(line), 3)]
if len(set(cards)) != len(cards):
    print('GRESKA')
    quit()
for card in cards:
    if card[0] == 'P':
        P.append(card[0])
    elif card[0] == 'K':
        K.append(card[0])
    elif card[0] == 'H':
        H.append(card[0])
    elif card[0] == 'T':
        T.append(card[0])

print(13-len(P), 13-len(K),13-len(H),13-len(T))