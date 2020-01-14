import time as t
import math as m

def prime(n):
	""" Return True if a number n is prime, "False" otherwise. """
	if n<=1:
		return False
	if n==2:
		return True
	if n%2==0:
		return False
	max_div = m.floor(m.sqrt(n))
	itera = m.floor(max_div / 2 + 1)
	for i in range(3, itera,  2):
		if n % i == 0  or n % (itera + 1) == 0:
			return False
	return True
