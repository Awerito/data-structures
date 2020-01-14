from primes import prime as p
import time as t
import math as m

array = []

def recprime(n):
	""" Count the primes recurrences in the index of the primes values """
	if array.count(n):
		return 1 + recprime(array.index(n) + 1)
	return 0

# Test
t0 = t.time()
maxi, i, value = 0, 0, 0
while(value < 10):
	i += 1
	if p(i):
		array.append(i)
		aux = recprime(i) 
		if aux > value:
			value = aux
			maxi = i
			print(maxi, ":", value)
t1 = t.time()
print(t1-t0)
