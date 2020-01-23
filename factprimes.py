from sequences.primes import prime as pr

cache = {0:2, 1:3}
def fact(n, a = []):
	""" Return an array with all the prime factors of n """
	if n == 1:
		return a
	for i in cache:
		if n == cache[i]:
			a.append(n)
			return fact(1, a)
	aux = cache[len(cache) - 1]
	if n > aux:
		for i in range(aux + 2, n + 1, 2):
			if pr(i):
				cache[len(cache)] = i
	for p in cache:
		if n % cache[p] == 0:
			a.append(cache[p])
			return fact(int(n / cache[p]), a)
