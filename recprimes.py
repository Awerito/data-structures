from primes import prime as p

def recprime(n, h=0):
	""" Return the consecutive primes of a number """
	if p(n):
		c = 1
		for i in range(1, n):
			if p(i):
				c += 1
		return 1 + recprime(c, h)
	return h

record, index, maxi = 0, 1, 0
while record < 10:
	aux = recprime(index)
	if aux > maxi:
		maxi = aux
		print(index, ":", maxi)
		record += 1
	index += 1

print(index, ":", maxi)
