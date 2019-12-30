import time as t
import math as m

def ifPrime(n):
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

#=====Test=====
t0 = t.time()
for n in range(1,100001):
	ifPrime(n)
t1 = t.time()
print("Time function: ", t1 - t0)
