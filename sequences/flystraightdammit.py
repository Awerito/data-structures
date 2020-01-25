import matplotlib.pyplot as plt

cache = {}
def gcd(a, b):
	""" Return the greatest common divisor between a and b """
	if b:
		return gcd(b, a % b)
	return a

def coprime(a, b):
	""" Return True if a and b are coprimes. False otherwise """
	if gcd(a, b) == 1:
		return True
	return False

def a(n):
	""" Return the n therm of the sequence https://oeis.org/A133058 """
	if n in cache:
		return cache[n]
	if n > 1:
		if coprime(n, a(n - 1)):
			aux = int(a(n - 1) + n + 1)
			cache[n] = aux
			return aux
		else:
			aux = int(a(n - 1) / gcd(n, a(n - 1)))
			cache[n] = aux
			return aux
	return 1

total = 800
x = list(range(0, total + 1))
y = []
for i in range(0, total + 1):
	y.append(a(i))

plt.plot(x, y, 'ro', markersize = 0.5)
plt.show()
