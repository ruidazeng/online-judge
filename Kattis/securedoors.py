N = int(input())
people = []

for _ in range(N):
    action, person = input().split()
    if action == "entry":
        if person in people:
            print(person, "entered", "(ANOMALY)")
        else:
            print(person, "entered")
            people.append(person)
    elif action == "exit":
        if person not in people:
            print(person, "exited", "(ANOMALY)")
        else:
            print(person, "exited")
            people.remove(person)