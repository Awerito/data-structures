cache = {}
def a(n):
	""" Return the n therm of the Stern sequence http://oeis.org/A002487 """
	if n in cache:
		return cache[n]
	if n == 0 or n == 1:
		return int(n)
	if n % 2 == 0:
		aux = int(a(n / 2))
		cache[n] = aux
		return aux
	else:
		aux = int(a((n - 1) / 2) + a((n + 1) / 2))
		cache[n] = aux
		return cache[n]
