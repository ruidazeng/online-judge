N = int(input())
answers = input()
    
strategy = {
    'Adrian': 'ABC',
    'Bruno': 'BABC',
    'Goran': 'CCAABB',
}

points = {}

for boy in strategy:
    boy_pts = 0
    
    # The zip() function will only iterate over the smallest list passed. 
    # If given lists of different lengths, the resulting combination
    # will only be as long as the smallest list passed. 
    
    for answer, guess in zip(answers, strategy[boy]*N):
        boy_pts += (answer == guess)
    points[boy] = boy_pts

best = max(points.values())
print(best)

# Need to be sorted since output the names in alphabetical order.
for boy in sorted(points):
    if points[boy] == best:
        print(boy)