n = int(input())
uni = []

for i in range(n):
    school, team = input().split()
    if school not in uni and len(uni) < 12:
        uni.append(school)
        print(school, team)