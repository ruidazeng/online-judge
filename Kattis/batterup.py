n = int(input())
numbers = map(int, input().split())

slug = []

for at_bat in numbers:
    if (at_bat != -1):
        slug.append(at_bat)

print(sum(slug)/len(slug))