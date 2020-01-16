import time as t

fib_cache = {}
phi = (1 + 5 ** (1 / 2)) / 2

def fibrecursive(n):
	""" Return the n therm of the Fibonacci sequence """
	if n in fib_cache:
		return fib_cache[n]
	if n == 1 or n == 2:
		return 1
	value = fibrecursive(n - 1) + fibrecursive(n - 2)
	fib_cache[n] = value
	return value

def fibonacci(n):
	""" Return the n therm of the Fibonacci sequence """
	return (phi**n - (1 - phi)**n) / (5**(1 / 2))

# Test
t0 = t.time()
for i in range(1, 10001):
	fibrecursive(i)
t1 = t.time()
print(t1 - t0)

t0 = t.time()
for i in range(1, 10001):
	fibonacci(i)
t1 = t.time()
print(t1 - t0)
