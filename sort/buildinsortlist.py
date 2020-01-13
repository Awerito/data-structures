import time as t
import random as rnd

s = []
for i in range(10001):
	s.append(rnd.randint(1, 100))

t0 = t.time()
s.sort()
t1 = t.time()

print(t1 - t0)

# 0.002005338668823242
