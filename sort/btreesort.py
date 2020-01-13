from btree import btree
import random as rnd
import time as t

#Test
tree = btree()
s = []
b = []
for i in range(10001):
	s.append(rnd.randint(1, 100))

t0 = t.time()
for i in s:
	tree.insert(i)

tree.sort(b)
t1 = t.time()

print(t1 - t0)

# 0.22058558464050293
