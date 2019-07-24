import math

DIAMATER = 60
SPEED = 15 # ft/sec

CIRCUM = math.pi * DIAMATER
INDEX = {c: i for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ '")}

def circular_distance(a, b):
    d = min(abs(INDEX[a] - INDEX[b]),
            len(INDEX) - abs(INDEX[a] - INDEX[b]))
    return CIRCUM * (d / len(INDEX))

n = int(input())

for _ in range(n):
    aphorism = input()
    time = len(aphorism) # Pick up time
    
    # The zip() function take iterables (can be zero or more),
    # makes iterator that aggregates elements based on
    # the iterables passed, and returns an iterator of tuples.
    
    for a, b in zip(aphorism, aphorism[1:]):
        time += circular_distance(a, b) / SPEED
        
    print(time)
    