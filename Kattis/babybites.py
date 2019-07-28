_ = int(input())
spoken = input().split()

count = 1
sense = True

for word in spoken:
    if word == 'mumble':
        count += 1
        continue
    else:
        word = int(word)
        if word != count:
            sense = False
            break
        count += 1
        

print("makes sense") if sense else print("something is fishy")