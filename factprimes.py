from primes import prime as pr

cache = {0:3}
def fact(n, a = {}):
	if n == 1:
		return a
	if n in cache:
		a[len(a)] = n
		return fact(1, a)
	if n % 2 == 0:
		a[len(a)] = 2
		return fact(n / 2, a)
	aux = cache[len(cache) - 1]
	if n > aux:
		for i in range(aux + 2, n + 1, 2):
			if pr(i):
				cache[len(cache)] = i
	for p in cache:
		if n % p == 0:
			a[len(a)] = p
			return fact(n / p, a)

# Test
print(fact(1))
print(fact(2))
print(fact(8))
