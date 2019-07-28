N = int(input())

for _ in range(N):
    gnomes = [int(x) for x in input().split()]
    tracker = gnomes[1]
    for index, gnome in enumerate(gnomes[1:-1]):
        if gnome != tracker:
            print(index + 1)
            break
        else:
            tracker += 1