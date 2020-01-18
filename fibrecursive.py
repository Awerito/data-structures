fib_cache = {}

def fibonacci(n):
	""" Return the n term of the Fibonacci sequence """
	if n in fib_cache:
		return fib_cache[n]
	if n == 1 or n == 2:
		return 1
	value = fibrecursive(n - 1) + fibrecursive(n - 2)
	fib_cache[n] = value
	return value
