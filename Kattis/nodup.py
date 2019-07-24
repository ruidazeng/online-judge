words = input().split()
unique = []
no_duplicate = True

for word in words:
    if word not in unique:
        unique.append(word)
    else:
        no_duplicate = False

print("yes") if no_duplicate else print("no")