import math

r = int(input())
euclid_area = math.pi * (r ** 2)

# A "circle" in taxicab geometry is essentially
# a square in Euclidean geoemtry due to the difference
# in the definition of distance between two points.

taxicab_area = 2.0 * (r ** 2)

print(euclid_area)
print(taxicab_area)