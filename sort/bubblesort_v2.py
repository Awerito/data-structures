import time as t
import random as rnd

def bubblesort(array):
	l = len(array)
	for i in range(len(array)):
		for j in range(l):
			if array[i] < array[j]:
				temp = array[i]
				array[i] = array[j]
				array[j] = temp
		l -= 1

#Test
s = []
for i in range(10001):
	s.append(rnd.randint(1, 100))

t0 = t.time()
s = bubblesort(s)
t1 = t.time()

print(t1 - t0)

# New time: 3.955472707748413
