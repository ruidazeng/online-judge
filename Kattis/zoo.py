index = 0

while True:
    n = int(input())
    index += 1 
    
    if n == 0:
        break
    
    zoo = {} # Python dictionaries
    
    for _ in range(n):
        animal = input().split()[-1].lower()
        if animal in zoo:
          zoo[animal] += 1 
        elif animal not in zoo:
            zoo[animal] = 1
    
    print("List " + str(index) + ':')
    
    for key in sorted(zoo.keys()):
        print(key, '|', zoo[key])