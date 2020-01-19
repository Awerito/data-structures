import matplotlib.pyplot as plt
import numpy as np
from time import time as t

plot = []
for i in range(1, 10001):
	t0 = t()
	# p(i)
	t1 = t()
	plot.append(t1 - t0)

plt.plot(plot)
plt.show()

