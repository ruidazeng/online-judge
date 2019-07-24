answer = input()
guess = input()

wrong = 0

for char in guess:
    if not answer:
        break
    elif char in answer:
        answer = answer.replace(char, '')
    else:
        wrong += 1
    

if wrong < 10:
    print("WIN")
else:
    print("LOSE")