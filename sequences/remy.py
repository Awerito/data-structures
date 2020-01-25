def a(n):
	r = 0
	for i in range(1, n):
		if n & i:
			r += 1
	return r
