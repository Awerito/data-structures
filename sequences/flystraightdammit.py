cache = {}
gcd = lambda a, b: gcd(b, a % b) if b else a
coprime = lambda a, b: True if gcd(a, b) == 1 else False
def a(n):
    """Return the n therm of the sequence https://oeis.org/A133058"""
    if n in cache:
        return cache[n]
    if n > 1:
        if coprime(n, a(n - 1)):
            aux = int(a(n - 1) + n + 1)
            cache[n] = aux
            return aux
        else:
            aux = int(a(n - 1) / gcd(n, a(n - 1)))
            cache[n] = aux
            return aux
    return 1

if __name__=="__main__":
    total = 100
    for i in range(1, total + 1):
        print(a(i))
