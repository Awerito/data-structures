import random, math

def distance(point1, point2):
	""" Return the distances between point1 and point2 """
	return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

# Estimate of the probability of P(x>pi/2)
obtuse = 0
total = 100000 

points = [[0, 0],[1, 0]]

for i in range(total + 1):
	a, b = 0, 0
	randpoint = [random.random(), random.random()]
	a, b = distance(points[0], randpoint), distance(points[1], randpoint) 
	angle = math.acos((a**2 + b**2 - 1) / (2*a*b))

	if angle > math.pi/2:
		obtuse += 1

print("P(x>pi/2) = ", obtuse / total)
