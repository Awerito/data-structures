def _fact(n, a):
    """Create and return the array of prime factors"""
    if n == 1:
        return [1]
    while n % 2 == 0:
        a.append(2)
        n = int(n / 2)
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            a.append(i)
            n = int(n / i)
    if n > 2:
        a.append(int(n))
    return a

def fact(n):
    """ Return the array of prime factors of n """
    return _fact(n, [])

if __name__=="__main__":
    for i in range(1, 101):
        print(fact(i))
