import matplotlib.pyplot as plt
import numpy as np
from random import random as rnd

logistic = lambda x, r: r*x*(1 - x)

def conv(x0, r, niter):
    x = x0
    for i in range(niter):
        x = logistic(x, r)
    return x

if __name__=="__main__":
    iterations = 100

    r_range = np.linspace(2.9, 4, 10**6)
    x = []

    for r in r_range:
        print(int((r - 2.9)/4*100), "%")
        x.append(conv(rnd(), r, iterations))

    plt.plot(r_range, x, ls='', marker=',')
    plt.show()
