import random as r

def flip():
	""" Return True or False random by 50% change """
	return True if r.random() > 0.5 else False

# Test
record, games = 0, 10001
for i in range(1, games + 1):
	if flip():
		record += 1
print(record / games)
