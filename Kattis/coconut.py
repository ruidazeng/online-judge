s, n = map(int, input().split())
hands = []

# represents players as a list of size-2 lists
for num in range(n):
    hands.append([num, "folded"])

i = 0  # starting point

while len(hands) != 1:

    # rhyme selects player (i + s - 1) mod n after player i
    i = (i + s - 1) % len(hands)

    if hands[i][1] == "folded":
        hands[i][1] = "fist"
        hands.insert(i + 1, [hands[i][0], "fist"])

    elif hands[i][1] == "fist":
        hands[i][1] = "palm"
        i = i + 1

    elif hands[i][1] == "palm":
        hands.pop(i)

print(hands[0][0] + 1)