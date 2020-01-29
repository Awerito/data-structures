from primes import prime as p
import concurrent.futures as cf
from time import time as t

def test(n):
    print(n, ":", p(n))

if __name__ == "__main__":
    threads = 1
    total = 1000000
    print("=============================")
    t0 = t()
    for i in range(1, total + 1):
        print(i, ":", p(i))
    t1 = t()
    print("Single-thread", t1 - t0)
    print("=============================")

    t0 = t()
    with cf.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(test, range(1, total + 1))
    t1 = t()
    print("Multi-thread", t1 - t0)
    print("=============================")
