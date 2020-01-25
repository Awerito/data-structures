import matplotlib.pyplot as p
from <++> import a

total = <++>
x = list(range(1, total + 1))
y = []

for i in range(1, total + 1):
	y.append(a(i))

p.plot(x, y, 'ro', markersize = 0.5)
p.show()
