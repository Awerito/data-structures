from sequences.primes import prime as p
def perf(n):
	""" Return "True" if the number n is a perfect number, "False" otherwise """
	if n == 1 or p(n):
		return False
	sum = 1
	for i in range(2, n):
		if n % i == 0:
			sum += i
			if n < sum:
				return False
	if sum == n:
		return True
	return False
