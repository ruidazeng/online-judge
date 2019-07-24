from math import pi
while True:
    r, m, c = input().split()
    if r == '0' and m == '0' and c == '0':
        break
    r = float(r)
    m, c = map(int, [m, c])
    true_area = pi * (r ** 2)
    # How large the circle is relative to the square.
    estimate_area = c/m * (2 * r) ** 2
    print(true_area, estimate_area)