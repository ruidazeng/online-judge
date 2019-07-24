import sys
from itertools import permutations

# The extend() extends the list by adding
# all items of a list (passed as an argument) to the end.

words = []
for l in sys.stdin.readlines():
    words.extend(l.split())

# Return successive r length permutations of elements in the iterable.
# If r is not specified or is None, then r defaults to the length
# of the iterable and all possible full-length permutations are generated.
# Permutations are emitted in lexicographic sort order.
# So, if the input iterable is sorted, the permutation
# tuples will be produced in sorted order.

unique_perms = set(''.join(word) for word in permutations(words, 2))
for word in sorted(unique_perms):
    print(word)