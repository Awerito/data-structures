def fact(n, a):
	while n % 2 == 0:
		a.append(2)
		n = int(n / 2)
	for i in range(3, int(n**0.5) + 1, 2):
		while n % i == 0:
			a.append(i)
			n = int(n / i)
	if n > 2:
		a.append(int(n))
	return a

