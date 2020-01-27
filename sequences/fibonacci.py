cache = {}
def a(n):
	""" Return the n term of the Fibonacci sequence """
	if n in cache:
		return cache[n]
	if n == 1 or n == 2:
		return 1
	value = a(n - 1) + a(n - 2)
	cache[n] = value
	return value

if __name__=="__main__":
    total = 10
    for i in range(1, total + 1):
        print(a(i))
