e, k, fact = 0, 0, 1
real = 2.71828182845904523536028
while real - 0.5 * e != 0:
	e += (k + 1) / fact
	k += 1
	fact *= k
print(k + 1)
