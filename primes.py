def prime(n):
	""" Return True if a number n is prime, "False" otherwise. """
	if n==2:
		return True
	if n<=1 or n%2==0:
		return False
	maxdiv = int(n ** (0.5)) + 1
	for i in range(3, maxdiv,  2):
		if n % i == 0:
			return False
	return True
