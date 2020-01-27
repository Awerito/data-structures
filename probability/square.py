from random import random as rnd
dist = lambda x1, y1, x2, y2: ((x1 - x2)**2 + (y1 - y2)**2)**0.5
sum = 0
total = 1000
for i in range(1, total + 1):
    x1, y1, x2, y2 = rnd(), rnd(), rnd(), rnd()
    sum += dist(x1, y1, x2, y2)
print(sum / total)
