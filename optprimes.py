import time as t
import math as m

array = []

def prime(n):
	""" Return True if a number n is prime, "False" otherwise. """
	if n==1:
		return False
	if n==2:
		return True
	if n>2 and n%2==0:
		return False

	max_div = m.floor(m.sqrt(n) + 1)
	for i in range(3, max_div, 2):
		if n % i == 0:
			return False
	return True

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
	if prime(i):
		array.append(i)
		aux = recprime(i) 
		if aux > value:
			value = aux
			maxi = i
			print(maxi, ":", value)
t1 = t.time()
print(t1-t0)
