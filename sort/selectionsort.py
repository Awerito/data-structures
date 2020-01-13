import time as t
import random as rnd

def selectionsort(array):
	l = len(array)
	for i in range(len(array)):
		biggest = 0
		index = 0
		for j in range(l):
			if array[j] > biggest:
				biggest = array[j]
				index = j
		l -= 1
		temp = array[index]
		array[index] = array[l]
		array[l] = temp
	return array

#Test
s = []
for i in range(10001):
	s.append(rnd.randint(1, 100))

t0 = t.time()
s = selectionsort(s)
t1 = t.time()

print(t1 - t0)
#3.0602688789367676
