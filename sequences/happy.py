def a(n):
	""" Return "True" if n is a happy number, "False" otherwise """
	if n == 1:
		return True
	if n == 4:
		return False
	sum = 0
	while n > 0:
		sum += (n % 10) ** 2
		n = int(n / 10)
	return a(sum)

if __name__=="__main__":
    total = 10
    for i in range(1, total + 1):
        print(i, ":", a(i))
