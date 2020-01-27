cache = {}
def a(n):
    if n in cache:
        return cache[n]
    if n > 2:
        aux = int(a(n - a(n - 1)) + a(n - a(n - 2)))
        cache[n] = aux
        return aux
    return 1

if __name__=="__main__":
    total = 100
    for i in range(1, total + 1):
        print(a(i))
