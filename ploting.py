import matplotlib.pyplot as plt
from factprimes2 import fact

def point(a):
	if a:
		if len(a) != len(set(a)):
			return 0
		if len(set(a)) % 2 == 0:
			return 1
		else:
			return -1
	return 0

total = 10000000
x = range(1, total + 1)
y2 = []
y3 = []
for i in x:
	aux = i**0.5
	y2.append(aux)
	y3.append(-aux)

y = []
factors = []
for i in range(total, 0, -1):
	factors.append(fact(i, []))
factors.reverse()

sum = 0
for i in range(0, total):
	sum += point(factors[i])
	y.append(sum)

plt.plot(x ,y, x, y2, x, y3)
plt.show()
