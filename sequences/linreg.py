mean = lambda array: sum(array) / len(array)
def linreg(x, y):
	""" Return the values [a, b] of the linear regression of x = [] and y = [] given y = a * x + b """
	xmean, ymean = mean(x), mean(y)
	num, den = 0, 0
	for i in range(len(x)):
		aux = (x[i] - xmean) 
		num += aux * (y[i] - ymean)
		den += aux**2
	b = num / den
	a = ymean - b * xmean
	return [b, a]
