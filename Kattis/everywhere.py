t = int(input())

for _ in range(t):
    n = int(input())
    cities = []
    for _ in range(n):
        city = input()
        if city not in cities:
            cities.append(city)
    print(len(cities))