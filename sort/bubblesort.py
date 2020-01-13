import random as rnd
import time as t

def bubblesort(array):
	for i in range(len(array)):
		for j in range(len(array)):
			if array[i] < array[j]:
				temp = array[i]
				array[i] = array[j]
				array[j] = temp
	return array

#Test
s = []
for i in range(10001):
	s.append(rnd.randint(1, 100))

t0 = t.time()
s = bubblesort(s)
t1 = t.time()

print(t1 - t0)
