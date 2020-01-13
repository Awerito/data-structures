term = lambda x: 16**-x * (4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6))
real, pi, count = 3.14159265358979323846264, 0, 0
while real - pi != 0:
	pi += term(count)
	count += 1
print(count, pi)
