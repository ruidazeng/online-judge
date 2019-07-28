def memoize(f):
    cache= {}
    def memf(*x):
        if x not in cache:
            cache[x] = f(*x)
        return cache[x]
    return memf

P = int(input())
for K in range(1, P+1):
    k, m, n = map(int, input().split())

    @memoize
    def solve(n, maxK = 0):
        """
        n = m^k + m^k ... + m^k + m^{k-1} + ... + 1
        """
        if maxK == 0:
            return 1

        if maxK == 1:
            return n//m + 1

        p = m**maxK
        return sum(solve(n - i*p, maxK - 1) for i in range((n//p + 1)))

    p = 0
    while m**p <= n:
        p += 1

    print(k, solve(n, p-1))
 rss 