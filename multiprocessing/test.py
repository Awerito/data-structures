from multiprocessing import Pool
from primes import prime
from time import time as t

if __name__=="__main__":
    total = 10000000
    threads = 4
    
    t0 = t()
    with Pool(threads) as p:
        p.map(prime, range(1, total + 1))
    t1 = t()
    print(t1 - t0)
