from primes import prime as p

array = []

def recprime(n):
	if array.count(n):
		return 1 + recprime(array.index(n) + 1)
	return 0

maxi, i, value = 0, 0, 0
while(True):
	i += 1
	if p(i):
		array.append(i)
		aux = recprime(i) 
		if aux > value:
			value = aux
			maxi = i
			print(maxi, ":", value)

