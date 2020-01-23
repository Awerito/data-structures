import matplotlib.pyplot as plt
from time import time

def fact(n, a):
	while n % 2 == 0:
		a.append(2)
		n = int(n / 2)
	for i in range(3, int(n**0.5) + 1, 2):
		while n % i == 0:
			a.append(i)
			n = int(n / i)
	if n > 2:
		a.append(int(n))
	return a

p = []
for i in range(1, 100001):
	t0 = time()
	fact(i, [])
	t1 = time()
	p.append(t1 - t0)

plt.plot(p)
plt.show()
