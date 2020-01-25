cache = {}
def fibonacci(n):
	""" Return the n term of the Fibonacci sequence """
	if n in cache:
		return cache[n]
	if n == 1 or n == 2:
		return 1
	value = fibrecursive(n - 1) + fibrecursive(n - 2)
	cache[n] = value
	return value
