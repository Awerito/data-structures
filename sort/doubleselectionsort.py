import time as t
import random as rnd

def selectionsort(array):
	l = len(array)
	b = 0
	for i in range(len(array)):
		biggest = 0
		bindex = i
		smallest = 101
		sindex = i
		for j in range(b, l):
			if array[j] > biggest:
				biggest = array[j]
				bindex = j
			if array[j] < smallest:
				smallest = array[j]
				sindex = j
		l -= 1
		temp = array[bindex]
		array[bindex] = array[l]
		array[l] = temp

		temp = array[sindex]
		array[sindex] = array[b]
		array[b] = temp
		b += 1
	return array

#Test
s = []
for i in range(10001):
	s.append(rnd.randint(1, 100))

t0 = t.time()
s = selectionsort(s)
t1 = t.time()

print(t1 - t0)
# 2.5593764781951904
