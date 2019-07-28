import sys, math

guess = 500

TOP = 1000
BOT = 0

while True:
    print(math.ceil(guess))
    sys.stdout.flush()
    
    response = input()
    if response == 'correct':
        quit()
    elif response == 'higher':
        BOT = guess
        guess = (guess + (TOP - guess)/2)
    elif response == 'lower':
        TOP = guess
        guess = (guess - (guess - BOT)/2)