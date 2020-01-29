from multiprocessing import Pool
from primes import prime
from time import time as t

if __name__=="__main__":
    total = 10000000
    threads = 4
    
    print("Single core:")
    t0 = t()
    for i in range(1, total + 1):
        prime(i)
    t1 = t()
    print(t1 - t0)

    print("Multi core:")
    t0 = t()
    with Pool(threads) as p:
        a = p.map(prime, range(1, total + 1))
    t1 = t()
    print(t1 - t0)
