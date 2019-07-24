l, r = map(int, input().split())

if l == 0 and r == 0:
    print("Not a moose")
elif l == r:
    print("Even", 2 * l)
elif l != r:
    print("Odd", 2 * max(l, r))