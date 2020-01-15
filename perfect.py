from primes import prime as p
import time as t

def perf(n):
	if n == 1 or p(n):
		return False
	sum = 1
	for i in range(2, n):
		if n % i == 0:
			sum += i
	if sum == n:
		return True
	return False

i, count = 1, 0
t0 = t.time()
while count < 4:
	if perf(i):
		count += 1
	i += 1
t1 = t.time()
print(t1 - t0)
