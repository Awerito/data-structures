cache = {0:1}
def factorial(n):
    """Return n!"""
    if n in cache:
        return cache[n]
    aux = n * factorial(n - 1)
    cache[n] = aux
    return aux

if __name__=="__main__":
    total = 100
    for i in range(1, total + 1):
        print(factorial(i))
