import matplotlib.pyplot as plt
from factprimes import fact as f

x = list(range(1, 100001))
y = list(map(lambda x: len(f(x, [])), range(1, 100001)))

plt.plot(x, y)
plt.show()
