def recprime(n):
    """ Count the primes recurrences in the index of the primes values """
    if array.count(n):
        return 1 + recprime(array.index(n) + 1)
    return 0
