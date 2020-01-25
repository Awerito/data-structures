import matplotlib.pyplot as plt
from primes import prime as p

f = lambda n: n - int(bin(n)[:1:-1],2)

total = 100001
primes = [2]
for i in range(3, total + 1, 2):
	if p(i):
		primes.append(i)

x = list(range(1, len(primes) + 1))
y = list(map(f, primes))

plt.plot(x, y, 'ro', markersize = 0.5)
plt.show()
