def prime(n):
    """Return True if n is primes, False otherwise"""
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    maxdiv = int(n ** (0.5)) + 1
    for i in range(3, maxdiv, 2):
        if n % i == 0:
            return False
    return True

if __name__=="__main__":
    total = 100
    for i in range(1, total + 1):
        print(i, ":", prime(i))
