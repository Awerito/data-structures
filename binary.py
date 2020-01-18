def conv(x, m, n):
	""" Return the x in base m to base n """
	c, i= 0, 0
	while x > 0:
		c += (m**i) * (x % n)
		x = int(x / n)
		i += 1
	return c
