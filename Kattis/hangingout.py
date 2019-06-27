l, x = map(int, input().split())
people = 0
not_allowed = 0

for _ in range(x):
    descri, p = input().split()
    p = int(p)
    if descri == "enter":
        if people + p > l:
            not_allowed += 1
        else:
            people += p
    elif descri == "leave":
        people -= p

print(not_allowed)