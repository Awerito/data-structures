def fact(n, a):
    """ Return an array with the prime factors of n """
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

if __name__=="__main__":
    for i in range(2, 101):
        print(fact(i, []))
